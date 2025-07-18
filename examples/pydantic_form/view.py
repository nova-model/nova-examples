"""View for Pydantic form example."""

from nova.mvvm.trame_binding import TrameBinding
from nova.trame import ThemedApp
from nova.trame.view.components import InputField
from nova.trame.view.layouts import GridLayout
from trame.widgets import html
from trame.widgets import vuetify3 as vuetify

from .model import Model
from .view_model import ViewModel


class App(ThemedApp):
    """View for Pydantic form example."""

    def __init__(self) -> None:
        super().__init__()

        self.create_vm()
        # If you forget to call connect, then the application will crash when you attempt to update the view.
        self.view_model.form_data_bind.connect("data")
        self.view_model.form_state_bind.connect("state")
        # Generally, we want to initialize the view state before creating the UI for ease of use. If initialization
        # is expensive, then you can defer it. In this case, you must handle the view state potentially being
        # uninitialized in the UI via v_if statements.
        self.view_model.update_form_data()
        self.view_model.update_form_state()

        self.create_ui()

    def create_ui(self) -> None:
        with super().create_ui() as layout:
            with layout.content:
                with vuetify.VCard(classes="mx-auto my-4", max_width=600):
                    with GridLayout(columns=2, gap="0.5em"):
                        # The GUI must bind the Pydantic model fields to elements.
                        # Most bindings use the tuple syntax: (parameter_name, default_value).
                        # If you don't have a default value, then you can use: (parameter_name,).
                        InputField(v_model=("data.user_name",))

                        # v_model allows you to just pass the parameter_name as a string.
                        # This typically does not work when binding other parameters.
                        InputField(v_model="data.domain_name")

                        # Try just passing a string to model_value, and see what happens here!
                        InputField(
                            model_value=("data.email",), column_span=2, label="Computed Email Address", readonly=True
                        )

                        # If you need to trigger some Python code on an event, then you can call view model functions
                        # directly.
                        vuetify.VBtn(
                            "Submit",
                            column_span=2,
                            disabled=("state.submit_disabled",),
                            click=self.view_model.submit,
                        )

                    # This is less common, but you can use handlebars expressions to display the form data inside of
                    # a string.
                    html.Span("You've submitted the following email address: {{ data.email }}", v_if="state.submitted")

    def create_vm(self) -> None:
        binding = TrameBinding(self.state)

        model = Model()
        self.view_model = ViewModel(model, binding)
