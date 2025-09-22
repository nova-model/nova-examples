"""View for NDIP workflow example."""

from nova.mvvm.trame_binding import TrameBinding
from nova.trame import ThemedApp
from nova.trame.view.components import InputField
from nova.trame.view.layouts import HBoxLayout
from trame.widgets import html
from trame.widgets import vuetify3 as vuetify

from .model import Model
from .view_model import ViewModel


class App(ThemedApp):
    """View for NDIP workflow example."""

    def __init__(self) -> None:
        super().__init__()

        self.create_vm()
        # If you forget to call connect, then the application will crash when you attempt to update the view.
        self.view_model.form_data_bind.connect("data")
        self.view_model.view_state_bind.connect("state")
        # Generally, we want to initialize the view state before creating the UI for ease of use. If initialization
        # is expensive, then you can defer it. In this case, you must handle the view state potentially being
        # uninitialized in the UI via v_if statements.
        self.view_model.update_form_data()

        self.create_ui()

    def create_ui(self) -> None:
        with super().create_ui() as layout:
            with layout.content:
                with vuetify.VCard(classes="mx-auto my-4 pa-1", max_width=600):
                    with HBoxLayout(classes="mb-2", gap="0.5em", valign="center"):
                        InputField(v_model="data.input_path")
                        with vuetify.VBtn(
                            disabled=("state.running || state.errors",), click=self.view_model.run_workflow
                        ):
                            vuetify.VProgressCircular(v_if="state.running", indeterminate=True, size=16)
                            html.Span("Run Workflow", v_else=True)

                    html.Span("Workflow Completed!", v_if="data.complete")

    def create_vm(self) -> None:
        binding = TrameBinding(self.state)

        model = Model()
        self.view_model = ViewModel(model, binding)
