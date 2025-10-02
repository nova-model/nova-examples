"""View for complex Pydantic rules example."""

from nova.mvvm.trame_binding import TrameBinding
from nova.trame import ThemedApp
from nova.trame.view.components import InputField
from nova.trame.view.layouts import VBoxLayout
from trame.widgets import vuetify3 as vuetify

from .model import Model
from .view_model import ViewModel


class App(ThemedApp):
    """View for complex Pydantic rules example."""

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
                    with VBoxLayout(columns=3, gap="0.5em"):
                        InputField(v_model="data.text", type="textarea")
                        InputField(v_model="data.tokenized_text", readonly=True, type="textarea")

    def create_vm(self) -> None:
        binding = TrameBinding(self.state)

        model = Model()
        self.view_model = ViewModel(model, binding)
