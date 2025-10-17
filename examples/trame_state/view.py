"""View for Trame state example."""

from nova.mvvm.trame_binding import TrameBinding
from nova.trame import ThemedApp
from nova.trame.view.layouts import VBoxLayout
from trame.widgets import vuetify3 as vuetify

from .view_model import ViewModel


class App(ThemedApp):
    """View for Trame state example."""

    def __init__(self) -> None:
        super().__init__()

        self.create_vm()
        # If you forget to call connect, then the application will crash when you attempt to update the view.
        self.view_model.view_state_bind.connect("view_state")

        self.create_ui()

    def create_ui(self) -> None:
        with super().create_ui() as layout:
            with layout.content:
                with VBoxLayout(halign="center", valign="center", stretch=True):
                    vuetify.VBtn("Open the Dialog", click=self.view_model.open_dialog)

                # Occasionally, we need to manually synchronize the view with the view model. This is necessary in Trame
                # when a Pydantic field is being changed without our InputField component.

                # When we need to manually synchronize the view and view model, we can use the below setup.
                # update_modelValue will trigger when the component changes the field, and flushState will manually send
                # the new value to the view model. To see the importance of this step, comment out the update_modelValue
                # call and try to dismiss the dialog.
                with vuetify.VDialog(
                    v_model="view_state.dialog_open", width=400, update_modelValue="flushState('view_state');"
                ):
                    with vuetify.VCard(classes="pa-4"):
                        vuetify.VCardTitle("Dialog")
                        vuetify.VCardSubtitle("Click anywhere outside of the dialog to dismiss.")

    def create_vm(self) -> None:
        binding = TrameBinding(self.state)

        self.view_model = ViewModel(binding)
