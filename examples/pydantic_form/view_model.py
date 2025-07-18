"""View model implementation for Pydantic form example."""

from typing import Any

from nova.mvvm.interface import BindingInterface

from .model import Model


class ViewModel:
    """View model implementation for Pydantic form example."""

    def __init__(self, model: Model, binding: BindingInterface) -> None:
        self.model = model
        # self.on_update is called any time the view updates the binding.
        self.form_bind = binding.new_bind(self.model.form, callback_after_update=self.on_update)

    def on_update(self, results: Any) -> None:
        print("The user has modified the form:", results)

        # If you need to detect that a specific field in the Pydantic model was updated, you can do so with:
        updated = results.get("updated", [])
        for update in updated:
            match update:
                case "user_name" | "domain_name":
                    self.model.unsubmit()
                    # In these cases, our computed field will update, and we need to communicate that update to the
                    # front-end. Try commenting this out and see what happens!
                    self.update_view()

    def submit(self) -> None:
        self.model.submit()
        # Now, the Pydantic model has the new value, but the view doesn't until we call update_view.
        self.update_view()

    def update_view(self) -> None:
        # This will fail if you haven't called connect on the binding!
        self.form_bind.update_in_view(self.model.form)
