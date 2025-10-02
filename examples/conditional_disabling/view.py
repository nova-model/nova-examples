"""View for conditional disabling example."""

from nova.mvvm.trame_binding import TrameBinding
from nova.trame import ThemedApp
from nova.trame.view.components import InputField
from nova.trame.view.layouts import GridLayout, HBoxLayout
from trame.widgets import vuetify3 as vuetify

from .model import Model
from .view_model import ViewModel


class App(ThemedApp):
    """View for conditional disabling example."""

    def __init__(self) -> None:
        super().__init__()

        self.create_vm()
        # If you forget to call connect, then the application will crash when you attempt to update the view.
        self.view_model.form_data_bind.connect("data")
        # Generally, we want to initialize the view state before creating the UI for ease of use. If initialization
        # is expensive, then you can defer it. In this case, you must handle the view state potentially being
        # uninitialized in the UI via v_if statements.
        self.view_model.update_form_data()

        self.create_ui()

    def create_ui(self) -> None:
        with super().create_ui() as layout:
            with layout.content:
                with vuetify.VCard(classes="mx-auto my-4", max_width=600):
                    with GridLayout(columns=2, classes="mb-2", gap="0.5em"):
                        InputField(v_model="data.email_address")
                        InputField(v_model="data.full_name")

                    with HBoxLayout(gap="0.5em", valign="center"):
                        InputField(v_model="data.disable_phone_field", type="checkbox")

                        # Now, we can use disable_phone_field to conditionally disable the phone number field.
                        # Note that because we need to bind to a parameter that doesn't start with v_ (indicating a
                        # v-directive in Vue.js), we need to use the Trame tuple syntax to bind to disabled.
                        InputField(v_model="data.phone_number", disabled=("data.disable_phone_field",))

    def create_vm(self) -> None:
        binding = TrameBinding(self.state)

        model = Model()
        self.view_model = ViewModel(model, binding)
