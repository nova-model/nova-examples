"""View model implementation for NDIP tool example."""

import os
from typing import Any, Dict

from blinker import signal
from nova.common.job import WorkState
from nova.common.signals import Signal, get_signal_id
from nova.galaxy.tool_runner import ToolRunner
from nova.mvvm.interface import BindingInterface

from .model import FractalsTool, Model


class ViewModel:
    """View model implementation for NDIP tool example."""

    def __init__(self, model: Model, binding: BindingInterface) -> None:
        # You must set these environment variables for this example to run. Please see the tutorial at
        # https://nova.ornl.gov/tutorial for instructions on how to set these environment variables. Note that when a
        # NOVA application is deployed to NDIP, we will automatically set these environment variables for you.
        galaxy_url = os.environ.get("GALAXY_URL", "https://calvera-test.ornl.gov")
        galaxy_api_key = os.environ.get("GALAXY_API_KEY", None)
        if not galaxy_url or not galaxy_api_key:
            raise EnvironmentError("GALAXY_URL and GALAXY_API_KEY must be set to run this example.")

        self.model = model

        self.form_data_bind = binding.new_bind(self.model.form)
        self.stats_bind = binding.new_bind(self.model.stats)

        # Using the ToolRunner will allow the tool's progress to be automatically communicated to the view.
        self.tool = FractalsTool(model)
        # The "fractals" string needs to be consistent with the view components.
        self.tool_runner = ToolRunner("fractals", self.tool, self.store_factory, galaxy_url, galaxy_api_key)

        # Now we need to listen for when the tool finished running.
        self.completion_signal = signal(get_signal_id("fractals", Signal.PROGRESS))
        self.completion_signal.connect(self.on_completion, weak=False)

    async def on_completion(self, _sender: Any, state: WorkState, details: Dict[str, Any]) -> None:
        if state == WorkState.FINISHED:
            self.tool.compute_stats()
            self.stats_bind.update_in_view(self.model.stats)

    def store_factory(self) -> str:
        # This will cause a history named "fractals" to be created on NDIP to store the tool's outputs, errors, and
        # results.
        return "fractals"

    def update_form_data(self) -> None:
        # This will fail if you haven't called connect on the binding!
        self.form_data_bind.update_in_view(self.model.form)
