"""View for ONCat example."""

from nova.mvvm.trame_binding import TrameBinding
from nova.trame import ThemedApp
from nova.trame.view.components.ornl import NeutronDataSelector
from nova.trame.view.layouts import VBoxLayout
from trame.widgets import html

from .model import Model
from .view_model import ViewModel


class App(ThemedApp):
    """View for ONCat example."""

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
                with VBoxLayout(stretch=True):
                    # You must set the ONCAT_CLIENT_ID and ONCAT_CLIENT_SECRET environment variables for this to
                    # work locally. If you don't know how to set them, then please visit https://oncat.ornl.gov/ and
                    # review the documentation or reach out to ONCat support for assistance. When this runs in
                    # production, we will set the environment for you automatically.
                    NeutronDataSelector(
                        v_model="data.selected_files",
                        base_paths=["/HFIR", "/SNS"],
                        classes="mb-1",
                        # This triggers the NeutronDataSelector to pull data from ONCat.
                        data_source="oncat",
                        # ONCat by default will return a large amount of metadata for each file. This can be
                        # extremely slow, so we strongly recommend setting the projection attribute to restrict the
                        # metadata to only what you need. This parameter matches the ONCat projection parameter
                        # exactly.
                        projection=["indexed.run_number"],
                        # You can uncomment the below lines to restrict data selection to a specific instrument.
                        # facility="SNS",
                        # instrument="TOPAZ",
                    )
                html.Span("You have selected {{ data.selected_files.length }} files.")

    def create_vm(self) -> None:
        binding = TrameBinding(self.state)

        model = Model()
        self.view_model = ViewModel(model, binding)
