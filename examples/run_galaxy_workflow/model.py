"""Model implementation for Galaxy workflow example."""

from enum import Enum
from typing import Callable

from nova.galaxy.connection import Connection
from nova.galaxy.workflow import Workflow, WorkflowParameters
from pydantic import BaseModel, Field, field_validator


class FractalOptions(str, Enum):
    """Defines options for the fractal_type field."""

    mandelbrot = "Mandelbrot Set"
    julia = "Julia Set Animation"
    random = "Random Walk"
    markus = "Markus-Lyapunov Fractal"


class FormData(BaseModel):
    """Pydantic model for the form data."""

    input_path: str = Field(default="", title="Analysis Cluster File to Ingest")

    @field_validator("input_path", mode="after")
    @classmethod
    def validate_input_path(cls, input_path: str) -> str:
        if not input_path.startswith("/SNS") and not input_path.startswith("/HFIR"):
            raise ValueError("File path must start with /SNS or /HFIR.")

        return input_path


class Model:
    """Model implementation for Galaxy workflow example."""

    def __init__(self) -> None:
        self.form = FormData()

    def run_workflow(self, galaxy_url: str, galaxy_api_key: str, progress: Callable) -> None:
        # You can call the progress method to inform the view model as progress is made in this function if needed.
        nova_instance = Connection(galaxy_url, galaxy_api_key)
        with nova_instance.connect() as conn:
            data_store = conn.get_data_store("workflow_test")

            # This allows us to retrieve a workflow by it's name for readability.
            workflows = conn.galaxy_instance.workflows.get_workflows(
                name="simple_test_workflow_with_dataset", published=True
            )
            workflow_id = workflows[0]["id"]
            workflow = Workflow(id=workflow_id)

            # We can add parameters similar to tools, but we must make sure that we label which step in the workflow the
            # parameter is for.
            params = WorkflowParameters()
            params.add_workflow_input("0", True)
            params.add_step_param("1", "params|ingest_mode", "file")
            params.add_step_param("1", "params|filepath", self.form.input_path)

            workflow.run(data_store=data_store, params=params, wait=True)
