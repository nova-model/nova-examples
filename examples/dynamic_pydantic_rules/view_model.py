"""View model implementation for dynamic Pydantic rules example."""

from nova.mvvm.interface import BindingInterface

from .model import Model


class ViewModel:
    """View model implementation for dynamic Pydantic rules example."""

    def __init__(self, model: Model, binding: BindingInterface) -> None:
        self.model = model

        # self.on_update is called any time the view updates the binding.
        self.form_data_bind = binding.new_bind(self.model.form)

    def update_form_data(self) -> None:
        # This will fail if you haven't called connect on the binding!
        self.form_data_bind.update_in_view(self.model.form)
