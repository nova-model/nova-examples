"""Main view for multitab example."""

from nova.mvvm.trame_binding import TrameBinding
from nova.trame import ThemedApp
from trame.widgets import vuetify3 as vuetify

from ..model import InputModel, StatsModel
from ..view_model import InputViewModel, MainViewModel, StatsViewModel
from .input import InputTab
from .stats import StatsTab


class App(ThemedApp):
    """Main view for multitab example."""

    def __init__(self) -> None:
        super().__init__()

        self.create_vm()
        self.main_vm.view_state_bind.connect("view_state")
        self.input_vm.inputs_bind.connect("inputs")
        self.stats_vm.stats_bind.connect("stats")

        self.input_vm.update_stats()

        self.create_ui()

    def create_ui(self) -> None:
        with super().create_ui() as layout:
            with layout.pre_content:
                with vuetify.VTabs(
                    v_model="view_state.active_tab", classes="pl-8", update_modelValue="flushState('view_state')"
                ):
                    vuetify.VTab("Input", value=0)
                    vuetify.VTab("Statistics", value=1)

            with layout.content:
                InputTab(v_if="view_state.active_tab == 0")
                StatsTab(v_if="view_state.active_tab == 1")

    def create_vm(self) -> None:
        binding = TrameBinding(self.state)

        self.main_vm = MainViewModel(binding)
        input_model = InputModel()
        self.input_vm = InputViewModel(input_model, binding)
        stats_model = StatsModel()
        self.stats_vm = StatsViewModel(stats_model, binding)
