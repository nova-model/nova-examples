"""View model implementation for Matplotlib example."""

from typing import Any, Dict

from matplotlib.figure import Figure
from nova.mvvm.interface import BindingInterface

from .model import Model


class ViewModel:
    """View model implementation for Matplotlib example."""

    def __init__(self, model: Model, binding: BindingInterface) -> None:
        self.model = model

        self.figure = Figure(layout="tight")
        self.ax = self.figure.subplots()

        self.figure_bind = binding.new_bind()
        self.plot_data_bind = binding.new_bind(self.model.plot_data, callback_after_update=self.on_update)

    def get_updated_figure(self) -> Figure:
        return self.figure

    def init_view(self) -> None:
        # This will fail if you haven't called connect on the binding!
        self.plot_data_bind.update_in_view(self.model.plot_data)

    def on_update(self, results: Dict[str, Any]) -> None:
        if results.get("updated", []):
            self.render_figure()
            self.figure_bind.update_in_view(None)

    def render_figure(self) -> None:
        self.ax.clear()
        self.ax.plot(self.model.get_data())
