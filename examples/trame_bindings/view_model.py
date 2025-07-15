"""View model implementation for Trame bindings example."""

from typing import Any

from nova.mvvm.interface import BindingInterface

from .model import Model


class ViewModel:
    """View model implementation for Trame bindings example."""

    def __init__(self, model: Model, binding: BindingInterface) -> None:
        self.model = model
        # self.on_update is called any time the view updates the binding.
        self.model_bind = binding.new_bind(self.model.pydantic, callback_after_update=self.on_update)

    def on_click(self) -> None:
        self.model.increment_button_clicks()
        # Now, the Pydantic model has the new value, but the view doesn't until we call update_view.
        self.update_view()

    def on_update(self, results: Any) -> None:
        print(results)

        # If you need to detect that a specific field in the Pydantic model was updated, you can do so with:
        updated = results.get("updated", [])
        if "title" in updated:
            print("new title:", self.model.get_title())

    def update_view(self) -> None:
        # This will fail if you haven't called connect on the binding!
        self.model_bind.update_in_view(self.model.pydantic)
