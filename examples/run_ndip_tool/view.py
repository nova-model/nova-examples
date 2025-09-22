"""View for NDIP tool example."""

from nova.mvvm.trame_binding import TrameBinding
from nova.trame import ThemedApp
from nova.trame.view.components import ExecutionButtons, InputField, ProgressBar, ToolOutputWindows
from nova.trame.view.layouts import VBoxLayout
from trame.widgets import html
from trame.widgets import vuetify3 as vuetify

from .model import Model
from .view_model import ViewModel


class App(ThemedApp):
    """View for NDIP tool example."""

    def __init__(self) -> None:
        super().__init__()

        self.create_vm()
        # If you forget to call connect, then the application will crash when you attempt to update the view.
        self.view_model.form_data_bind.connect("data")
        self.view_model.stats_bind.connect("stats")
        # Generally, we want to initialize the view state before creating the UI for ease of use. If initialization
        # is expensive, then you can defer it. In this case, you must handle the view state potentially being
        # uninitialized in the UI via v_if statements.
        self.view_model.update_form_data()

        self.create_ui()

    def create_ui(self) -> None:
        with super().create_ui() as layout:
            with layout.content:
                with vuetify.VCard(classes="mx-auto my-4 pa-1", max_width=600):
                    with VBoxLayout(gap="0.5em"):
                        InputField(v_model="data.fractal_type", type="select")

                        # These components add UI components for monitoring the job automatically.
                        # The "fractals" string needs to be consistent with the ToolRunner in the view model.
                        ProgressBar("fractals")
                        ToolOutputWindows("fractals")

                        with html.Div(v_if="stats.count.length > 0"):
                            html.P(
                                "PIL computed {{ stats.count.length }} bands for the generated fractal image.",
                                classes="mb-2",
                            )
                            html.P(
                                (
                                    "Band {{ index + 1 }} Stats: "
                                    "Count={{ stats.count[index] }}, "
                                    "Extrema={{ stats.extrema[index] }}, "
                                    "Mean={{ stats.mean[index] }}, "
                                    "Median={{ stats.median[index] }}"
                                ),
                                v_for="(_, index) in stats.count.length",
                            )

            with layout.post_content:
                # This adds UI components for running and stopping the tool.
                ExecutionButtons("fractals")

    def create_vm(self) -> None:
        binding = TrameBinding(self.state)

        model = Model()
        self.view_model = ViewModel(model, binding)
