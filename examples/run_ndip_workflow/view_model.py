"""View model implementation for NDIP workflow example."""

import os
from functools import partial
from typing import Any, Dict

from nova.mvvm.interface import BindingInterface
from pydantic import BaseModel, Field

from .model import Model


class ViewState(BaseModel):
    """Pydantic model for view state."""

    complete: bool = Field(default=False)
    errors: bool = Field(default=True)
    running: bool = Field(default=False)


class ViewModel:
    """View model implementation for NDIP workflow example."""

    def __init__(self, model: Model, binding: BindingInterface) -> None:
        # You must set these environment variables for this example to run. Please see the tutorial at
        # https://nova.ornl.gov/tutorial for instructions on how to set these environment variables. Note that when a
        # NOVA application is deployed to NDIP, we will automatically set these environment variables for you.
        self.galaxy_url = os.environ.get("GALAXY_URL", "https://calvera-test.ornl.gov")
        self.galaxy_api_key = os.environ.get("GALAXY_API_KEY", None)
        if not self.galaxy_url or not self.galaxy_api_key:
            raise EnvironmentError("GALAXY_URL and GALAXY_API_KEY must be set to run this example.")

        self.model = model
        self.binding = binding

        self.form_data_bind = binding.new_bind(self.model.form, callback_after_update=self.on_form_update)

        self.view_state = ViewState()
        self.view_state_bind = binding.new_bind(self.view_state)

    def on_completion(self) -> None:
        # Here, we can fetch and process outputs similar to the NDIP tool example. See the TOPAZ Reduction GUI for a
        # complete example including results processing for workflows.
        # https://code.ornl.gov/ndip/tool-sources/single-crystal-diffraction/topaz-data-reduction
        self.view_state.complete = True
        self.view_state.running = False
        self.update_view()

    def on_form_update(self, results: Dict[str, Any]) -> None:
        # This blocks running the workflow in the form inputs are invalid.
        if results.get("errored", []):
            self.view_state.errors = True
        else:
            self.view_state.errors = False

        self.update_view()

    def run_workflow(self) -> None:
        self.view_state.complete = False
        self.view_state.running = True
        self.update_view()

        # This runs the workflow in a background thread to avoid blocking the Trame server.
        worker = self.binding.new_worker(partial(self.model.run_workflow, self.galaxy_url, self.galaxy_api_key))
        worker.connect_finished(self.on_completion)
        worker.connect_progress(lambda *args: None)
        worker.start()

    def update_form_data(self) -> None:
        # This will fail if you haven't called connect on the binding!
        self.form_data_bind.update_in_view(self.model.form)

    def update_view(self) -> None:
        self.view_state_bind.update_in_view(self.view_state)
