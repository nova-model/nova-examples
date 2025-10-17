"""View for Pydantic/Monaco example."""

from nova.mvvm.trame_binding import TrameBinding
from nova.trame import ThemedApp
from nova.trame.view.layouts import VBoxLayout
from trame.widgets import client, code, html

from .model import Model
from .view_model import ViewModel


class App(ThemedApp):
    """View for Pydantic/Monaco example."""

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

        # The Monaco editor in Trame will not automatically scale to the size of its container. Since we typically want
        # behavior, you can add it with the following JavaScript.
        # This performs the scaling.
        self.scale_editor = "window.trame.refs.monaco_container.editor.layout()"
        # This instructs the browser to perform the scaling once immediately and again every time the browser is
        # resized. The setTimeout call delays the first scaling to give the editor time to initialize.
        self.start_scaling = (
            "window.setTimeout(() => {"
            f" {self.scale_editor};"
            f" window.addEventListener('resize', () => {{ {self.scale_editor} }});"
            "}, 100);"
        )

        self.create_ui()

    def create_ui(self) -> None:
        with super().create_ui() as layout:
            with layout.content:
                with VBoxLayout(stretch=True):
                    # If a component doesn't support the v_model parameter, as with the Monaco editor, then we can
                    # set the initial value and listen to the events manually.
                    code.Editor(
                        ref="monaco_container",
                        model_value=("data",),
                        language="json",
                        theme="vs-dark",
                        input=(self.view_model.on_input, "[$event]"),
                    )
                    # This injects our JavaScript snippet when the browser loads this content.
                    client.ClientTriggers(mounted=self.start_scaling)

                    html.P("{{ error }}", v_for="error in state.errors")

    def create_vm(self) -> None:
        binding = TrameBinding(self.state)

        model = Model()
        self.view_model = ViewModel(model, binding)
