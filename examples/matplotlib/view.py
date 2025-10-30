"""View for Matplotlib example."""

from typing import Any

from nova.mvvm.trame_binding import TrameBinding
from nova.trame import ThemedApp
from nova.trame.view.components import InputField
from nova.trame.view.components.visualization import MatplotlibFigure
from nova.trame.view.layouts import GridLayout, HBoxLayout

from .model import Model
from .view_model import ViewModel


class App(ThemedApp):
    """View for Matplotlib example."""

    def __init__(self) -> None:
        super().__init__()

        self.create_vm()
        # If you forget to call connect, then the application will crash when you attempt to update the view.
        self.view_model.figure_bind.connect(self.update_figure)
        self.view_model.plot_data_bind.connect("plot_data")
        # Generally, we want to initialize the view state before creating the UI for ease of use. If initialization
        # is expensive, then you can defer it. In this case, you must handle the view state potentially being
        # uninitialized in the UI via v_if statements.
        self.view_model.init_view()

        self.create_ui()

    def create_ui(self) -> None:
        with super().create_ui() as layout:
            with layout.content:
                with GridLayout(classes="mb-4", columns=2, gap="1em"):
                    InputField("plot_data.data_points")
                    InputField("plot_data.function", type="select")

                with HBoxLayout(classes="overflow-hidden", stretch=True):
                    # Try increasing the number of data points to something very large and observe the drop in
                    # performance. Then, set webagg to True and try again and see the difference. webagg is a
                    # server-side rendering mode for Matplotlib.
                    self.figure_view = MatplotlibFigure(figure=self.view_model.get_updated_figure(), webagg=False)

    def create_vm(self) -> None:
        binding = TrameBinding(self.state)

        model = Model()
        self.view_model = ViewModel(model, binding)

    def update_figure(self, _: Any = None) -> None:
        self.figure_view.update(self.view_model.get_updated_figure())
