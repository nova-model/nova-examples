"""View for Pydantic form with options example."""

from nova.mvvm.trame_binding import TrameBinding
from nova.trame import ThemedApp
from nova.trame.view.components import InputField
from nova.trame.view.layouts import HBoxLayout, VBoxLayout

from .model import Model
from .view_model import ViewModel


class App(ThemedApp):
    """View for Pydantic form with options example."""

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
                with VBoxLayout(gap="0.25em"):
                    with HBoxLayout(gap="0.25em", stretch=True):
                        # By setting type=select, NOVA will create a dropdown. Since the model for this field is typed
                        # as an Enum, the options will be automatically populated. The extra HBoxLayout here is
                        # optional. It's simply a way to instruct this InputField to shrink since stretch is not set to
                        # True.
                        with HBoxLayout():
                            InputField(v_model="data.phone_country", type="select")
                        InputField(v_model="data.phone_number")

                    # This checkbox will cause the dynamic list to be updated.
                    InputField(v_model="data.show_all_org_options", type="checkbox")
                    # Since data.organization uses a dynamic list of items, we must manually specify the items as below.
                    # Note that we use Trame's parameter binding syntax (the tuple) here to be clear that we intend this
                    # list to be dynamic.
                    InputField(v_model="data.organization", items=("data.org_options",), type="radio")

    def create_vm(self) -> None:
        binding = TrameBinding(self.state)

        model = Model()
        self.view_model = ViewModel(model, binding)
