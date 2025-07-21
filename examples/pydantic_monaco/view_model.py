"""View model implementation for Pydantic/Monaco example."""

from typing import List

from nova.mvvm.interface import BindingInterface
from pydantic import BaseModel, Field, ValidationError

from .model import Model


class FormState(BaseModel):
    """Pydantic model for the view state."""

    errors: List[str] = Field(default=[])


class ViewModel:
    """View model implementation for Pydantic/Monaco example."""

    def __init__(self, model: Model, binding: BindingInterface) -> None:
        self.model = model
        self.view_state = FormState()

        self.form_data_bind = binding.new_bind(self.model.form)
        self.form_state_bind = binding.new_bind(self.view_state)

    def on_input(self, json_data: str) -> None:
        # Monaco fires input events with internal data that need to be ignored.
        if "_vts" in json_data:
            return

        self.view_state.errors = []
        try:
            self.model.set_from_json(json_data)
        except ValidationError as e:
            for error in e.errors():
                msg = ""
                if error["loc"]:
                    msg += f"{error['loc'][0]}: "
                msg += error["msg"]

                self.view_state.errors.append(msg)

        self.update_form_state()

    def update_form_data(self) -> None:
        # This will fail if you haven't called connect on the binding!
        self.form_data_bind.update_in_view(self.model.form)

    def update_form_state(self) -> None:
        # This will fail if you haven't called connect on the binding!
        self.form_state_bind.update_in_view(self.view_state)
