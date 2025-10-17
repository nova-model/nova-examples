"""View for data selector example."""

import os

from nova.mvvm.trame_binding import TrameBinding
from nova.trame import ThemedApp
from nova.trame.view.components import DataSelector
from nova.trame.view.layouts import VBoxLayout
from trame.widgets import html

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
                with VBoxLayout(stretch=True):
                    # Please note that this is a dangerous operation. You should ensure that you restrict this
                    # component to only expose files that are strictly necessary to making your application
                    # functional.
                    DataSelector(
                        v_model="data.selected_files",
                        directory=os.environ.get("HOME", "/"),
                        classes="mb-1",
                    )
                html.Span("You have selected {{ data.selected_files.length }} files.")

    def create_vm(self) -> None:
        binding = TrameBinding(self.state)

        model = Model()
        self.view_model = ViewModel(model, binding)
