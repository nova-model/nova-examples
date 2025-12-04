"""View for file download example."""

import os
from typing import Optional

from nova.mvvm.trame_binding import TrameBinding
from nova.trame import ThemedApp
from nova.trame.view.components import DataSelector
from nova.trame.view.layouts import VBoxLayout
from trame.widgets import client
from trame.widgets import vuetify3 as vuetify

from .model import Model
from .view_model import ViewModel


class App(ThemedApp):
    """View for file download example."""

    def __init__(self) -> None:
        super().__init__()

        self.create_vm()
        # If you forget to call connect, then the application will crash when you attempt to update the view.
        self.view_model.form_data_bind.connect("data")
        # Generally, we want to initialize the view state before creating the UI for ease of use. If initialization
        # is expensive, then you can defer it. In this case, you must handle the view state potentially being
        # uninitialized in the UI via v_if statements.
        self.view_model.update_form_data()

        self._download: Optional[client.JSEval] = None

        self.create_ui()

    def create_ui(self) -> None:
        self.set_theme("CompactTheme")

        with super().create_ui() as layout:
            # TODO: move this into nova-trame
            self._download = client.JSEval(
                exec=(
                    "async ($event) => {"
                    "  const [filename, mimetype, content] = $event;"
                    "  const blob = new window.Blob([content], {type: mimetype});"
                    "  const url = window.URL.createObjectURL(blob);"
                    "  const anchor = window.document.createElement('a');"
                    "  anchor.setAttribute('href', url);"
                    "  anchor.setAttribute('download', filename);"
                    "  window.document.body.appendChild(anchor);"
                    "  anchor.click();"
                    "  window.document.body.removeChild(anchor);"
                    "  window.setTimeout(() => window.URL.revokeObjectURL(url), 1000);"
                    "}"
                )
            ).exec

            with layout.content:
                with VBoxLayout(classes="mb-2", stretch=True):
                    # Please note that this is a dangerous operation. You should ensure that you restrict this
                    # component to only expose files that are strictly necessary to making your application
                    # functional.
                    DataSelector(
                        v_model="data.selected_files",
                        directory=os.environ.get("HOME", "/"),
                        classes="mb-1",
                    )

                with VBoxLayout(halign="center"):
                    vuetify.VBtn("Download Selected Files", click=self.download_files)

    def create_vm(self) -> None:
        binding = TrameBinding(self.state)

        model = Model()
        self.view_model = ViewModel(model, binding)

    async def download_files(self) -> None:
        content = self.view_model.prepare_zip()
        if content and self._download:
            # TODO: call new nova-trame method here
            self._download(["selected_files.zip", "application/zip", content])
