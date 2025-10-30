"""View model implementation for Pydantic form with options example."""

from typing import Any

from nova.mvvm.interface import BindingInterface

from .model import Model


class ViewModel:
    """View model implementation for Pydantic form with options example."""

    def __init__(self, model: Model, binding: BindingInterface) -> None:
        self.model = model

        # self.on_update is called any time the view updates the binding.
        self.form_data_bind = binding.new_bind(self.model.form, callback_after_update=self.on_update)

    def on_update(self, results: Any) -> None:
        # print(results)
        for result in results.get("updated", []):
            match result:
                case "show_all_org_options":
                    # Now, we can update the dynamic options for the radio button group.
                    self.model.update_org_options()
                    self.update_form_data()

    def update_form_data(self) -> None:
        # This will fail if you haven't called connect on the binding!
        self.form_data_bind.update_in_view(self.model.form)
