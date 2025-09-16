"""Main view model."""

from nova.mvvm.interface import BindingInterface
from pydantic import BaseModel, Field


class ViewState(BaseModel):
    """Pydantic class for view state."""

    active_tab: int = Field(default=0)


class MainViewModel:
    """Main view model."""

    def __init__(self, binding: BindingInterface) -> None:
        self.view_state = ViewState()
        self.view_state_bind = binding.new_bind(self.view_state)
