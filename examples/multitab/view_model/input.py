"""View model for the input tab."""

from typing import Any

from nova.common.events import get_event
from nova.mvvm.interface import BindingInterface

from ..model.input import InputModel


class InputViewModel:
    """View model for the input tab."""

    def __init__(self, model: InputModel, binding: BindingInterface) -> None:
        self.model = model

        # self.on_update is called any time the view updates the binding.
        self.inputs_bind = binding.new_bind(self.model.inputs, callback_after_update=self.update_stats)

        # To communicate changes in this view model to other view models, we can create an event.
        self.update_event = get_event("inputs_updated")

    def update_stats(self, results: Any = None) -> None:
        # Now, we can send an event to all listening view models.
        self.update_event.send_sync(values=self.model.get_values())
