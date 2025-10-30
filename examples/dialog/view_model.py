"""View model implementation for dialog example."""

from nova.mvvm.interface import BindingInterface
from pydantic import BaseModel, Field


class ViewState(BaseModel):
    """Pydantic model for holding view state."""

    dialog_open: bool = Field(default=False)


class ViewModel:
    """View model implementation for dialog example."""

    def __init__(self, binding: BindingInterface) -> None:
        self.view_state = ViewState()

        self.view_state_bind = binding.new_bind(self.view_state)

    def open_dialog(self) -> None:
        self.view_state.dialog_open = True
        self.view_state_bind.update_in_view(self.view_state)
