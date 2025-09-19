"""Model implementation for NDIP tool example."""

from enum import Enum
from typing import Tuple

from nova.galaxy import Parameters, Tool
from nova.galaxy.interfaces import BasicTool
from pydantic import BaseModel, Field


class FractalOptions(str, Enum):
    """Defines options for the fractal_type field."""

    mandelbrot = "Mandelbrot Set"
    julia = "Julia Set Animation"
    random = "Random Walk"
    markus = "Markus-Lyapunov Fractal"


class FormData(BaseModel):
    """Pydantic model for the form data."""

    fractal_type: FractalOptions = Field(default=FractalOptions.mandelbrot, title="Type")


class Model:
    """Model implementation for NDIP tool example."""

    def __init__(self) -> None:
        self.form = FormData()


class FractalsTool(BasicTool):
    """Class that prepares IPS Fastran tool."""

    def __init__(self, model: Model) -> None:
        super().__init__()
        self.model = model

    def prepare_tool(self) -> Tuple[Tool, Parameters]:
        # Pass the fractal type dropdown value to the tool. The "option" name comes from the tool XML file.
        tool_params = Parameters()
        tool_params.add_input(name="option", value=self.model.form.fractal_type)

        # Create the tool.
        self.tool = Tool(id="neutrons_fractal")

        return self.tool, tool_params

    def get_results(self) -> None:
        # TODO: add some processing of the results.
        pass
