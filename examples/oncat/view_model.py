"""View model implementation for ONCat example."""

from typing import Any, Dict

from nova.mvvm.interface import BindingInterface

from .model import Model


class ViewModel:
    """View model implementation for ONCat example."""

    def __init__(self, model: Model, binding: BindingInterface) -> None:
        self.model = model

        # self.on_update is called any time the view updates the binding.
        self.form_data_bind = binding.new_bind(self.model.form, callback_after_update=self.on_update)

    def on_update(self, results: Dict[str, Any]) -> None:
        # This fires when the data selector is updated. You could run some process on the newly selected data or update
        # other portions of the UI here as necessary.
        print(f"Selected files updated: {self.model.get_selected_files()}")

    def update_form_data(self) -> None:
        # This will fail if you haven't called connect on the binding!
        self.form_data_bind.update_in_view(self.model.form)
