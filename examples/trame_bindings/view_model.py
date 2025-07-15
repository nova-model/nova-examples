"""View model implementation for Trame bindings example."""

from typing import Any

from nova.mvvm.interface import BindingInterface

from .model import Model


class ViewModel:
    """View model implementation for Trame bindings example."""

    def __init__(self, model: Model, binding: BindingInterface) -> None:
        self.model = model
        self.model_bind = binding.new_bind(self.model.pydantic, callback_after_update=self.on_update)

    def on_click(self) -> None:
        self.model.increment_button_clicks()
        self.update_view()

    def on_update(self, results: Any) -> None:
        updated = results.get("updated", [])
        if "title" in updated:
            print("title updated:", self.model.get_title())

    def update_view(self) -> None:
        self.model_bind.update_in_view(self.model.pydantic)
