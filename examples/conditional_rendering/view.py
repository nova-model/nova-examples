"""View for conditional rendering example."""

from nova.mvvm.trame_binding import TrameBinding
from nova.trame import ThemedApp
from nova.trame.view.components import InputField
from nova.trame.view.layouts import GridLayout, HBoxLayout, VBoxLayout
from trame.widgets import html
from trame.widgets import vuetify3 as vuetify

from .model import Model
from .view_model import ViewModel


class App(ThemedApp):
    """View for conditional rendering example."""

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
                with GridLayout(columns=2, classes="mb-2", gap="0.5em"):
                    InputField(v_model="data.email_address")
                    InputField(v_model="data.full_name")

                with HBoxLayout(classes="mb-2", gap="0.5em", valign="center"):
                    InputField(v_model="data.show_phone_field", type="checkbox")

                    # Now, we can use show_phone_field to conditionally render the phone number field.
                    InputField(v_if="data.show_phone_field", v_model="data.phone_number")
                    # Following a v_if, we can use v_else_if and v_else.
                    html.Span("{{ data.full_name }}'s phone number is hidden.", v_else_if="data.full_name")
                    html.Span("Phone number is hidden.", v_else=True)

                with VBoxLayout(gap="0.5em", stretch=True):
                    # We can also use v_show to conditionally render a field. Note that when using v_show, you won't
                    # be able to use v_else_if or v_else afterwards. There is a deeper discussion of the differences
                    # between v_if and v_show in the Vue.js documentation: https://vuejs.org/guide/essentials/conditional#v-if-vs-v-show.
                    vuetify.VBtn("Toggle Comments Field", click=self.view_model.toggle_comments)
                    InputField(v_show="data.show_comments_field", v_model="data.comments", type="textarea")

    def create_vm(self) -> None:
        binding = TrameBinding(self.state)

        model = Model()
        self.view_model = ViewModel(model, binding)
