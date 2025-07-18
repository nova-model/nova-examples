"""View model implementation for Pydantic form example."""

from typing import Any

from nova.mvvm.interface import BindingInterface
from pydantic import BaseModel, Field, computed_field

from .model import FormData, Model


class FormState(BaseModel):
    """Pydantic model for the view state."""

    block_submit: bool = Field(default=True)
    submitted: bool = Field(default=False)
    _data: FormData  # We need a reference to the data object to perform validation below

    @computed_field
    @property
    def submit_disabled(self) -> bool:
        if self.block_submit or "@" not in self._data.email:
            return True
        return False


class ViewModel:
    """View model implementation for Pydantic form example."""

    def __init__(self, model: Model, binding: BindingInterface) -> None:
        self.model = model
        self.view_state = FormState()
        self.view_state._data = self.model.form

        # self.on_update is called any time the view updates the binding.
        self.form_data_bind = binding.new_bind(self.model.form, callback_after_update=self.on_update)
        self.form_state_bind = binding.new_bind(self.view_state)

    def on_update(self, results: Any) -> None:
        print("The user has modified the form:", results)

        # If you need to detect that a specific field in the Pydantic model was updated, you can do so with:
        updated = results.get("updated", [])
        for update in updated:
            match update:
                case "user_name" | "domain_name":
                    self.view_state.submitted = False
                    # The computed field will recompute, and we need to communicate that update to the
                    # front-end. Try commenting this out and see what happens!
                    self.update_form_data()

        # You can also detect validation errors in the Pydantic model.
        errored = results.get("errored", [])
        self.view_state.block_submit = False
        if errored:
            self.view_state.block_submit = True
        self.update_form_state()

    def submit(self) -> None:
        self.view_state.submitted = True
        # Now, the Pydantic model has the new value, but the view doesn't until we call update_view.
        self.update_form_state()

    def update_form_data(self) -> None:
        # This will fail if you haven't called connect on the binding!
        self.form_data_bind.update_in_view(self.model.form)

    def update_form_state(self) -> None:
        # This will fail if you haven't called connect on the binding!
        self.form_state_bind.update_in_view(self.view_state)
