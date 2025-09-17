"""View for data selector example."""

from nova.mvvm.trame_binding import TrameBinding
from nova.trame import ThemedApp
from nova.trame.view.components.ornl import NeutronDataSelector
from nova.trame.view.layouts import VBoxLayout
from trame.widgets import html
from trame.widgets import vuetify3 as vuetify

from .model import Model
from .view_model import ViewModel


class App(ThemedApp):
    """View for data selector example."""

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
        self.set_theme("CompactTheme")

        with super().create_ui() as layout:
            with layout.content:
                with vuetify.VCard(classes="mx-auto my-4 pa-1", max_width=600):
                    with VBoxLayout(height=400):
                        # Please note that this example will not work locally if /HFIR and /SNS don't exist on your
                        # development machine. You can either simulate or try to mount them depending on your
                        # circumstances.
                        NeutronDataSelector(
                            v_model="data.selected_files",
                            base_paths=["/HFIR", "/SNS"],
                            classes="mb-1",
                            # You can uncomment the below lines to restrict data selection to a specific instrument.
                            # facility="SNS",
                            # instrument="TOPAZ",
                        )
                    html.Span("You have selected {{ data.selected_files.length }} files.")

    def create_vm(self) -> None:
        binding = TrameBinding(self.state)

        model = Model()
        self.view_model = ViewModel(model, binding)
