"""View for Trame bindings example."""

from nova.mvvm.trame_binding import TrameBinding
from nova.trame import ThemedApp
from nova.trame.view.components import InputField
from nova.trame.view.layouts import VBoxLayout
from trame.widgets import html
from trame.widgets import vuetify3 as vuetify

from examples.trame_bindings.mvvm_factory import create_vm


class App(ThemedApp):
    """View for Trame bindings example."""

    def __init__(self) -> None:
        super().__init__()

        binding = TrameBinding(self.state)

        self.view_model = create_vm(binding)
        self.view_model.model_bind.connect("pydantic")
        self.view_model.update_view()

        self.create_ui()

    def create_ui(self) -> None:
        with super().create_ui() as layout:
            with layout.content:
                # The title parameter to VCard uses a two-way binding (view <-> view model).
                # Most bindings use the tuple syntax: (parameter_name, default_value).
                # If you don't have a default value, then you can use: (parameter_name,).
                # Please make sure that the parameter_name matches the connect call in __init__.
                with vuetify.VCard(classes="mx-auto my-4", max_width=600, title=("pydantic.title",)):
                    with VBoxLayout(gap="0.5em"):
                        # The v_model parameter always produces a binding, so you can just pass a string with the
                        # parameter_name if you don't have a default value.
                        InputField(v_model="pydantic.title")

                        # One-way binding (view -> view model)
                        vuetify.VBtn("Click Me!", click=self.view_model.on_click)

                        # One-way binding (view model -> view)
                        html.Span("You have clicked the button {{ pydantic.button_clicks }} times.")
