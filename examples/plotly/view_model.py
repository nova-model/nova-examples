"""View model implementation for Plotly example."""

from typing import Any, Dict

import plotly.graph_objects as go
from nova.mvvm.interface import BindingInterface

from .model import Model


class ViewModel:
    """View model implementation for Plotly example."""

    def __init__(self, model: Model, binding: BindingInterface) -> None:
        self.model = model

        self.figure = go.Figure()

        self.figure_bind = binding.new_bind()
        self.plot_data_bind = binding.new_bind(self.model.plot_data, callback_after_update=self.on_update)

    def get_updated_figure(self) -> go.Figure:
        return self.figure

    def init_view(self) -> None:
        # This will fail if you haven't called connect on the binding!
        self.plot_data_bind.update_in_view(self.model.plot_data)

    def on_update(self, results: Dict[str, Any]) -> None:
        if results.get("updated", []):
            self.render_figure()
            self.figure_bind.update_in_view(None)

    def render_figure(self) -> None:
        self.figure.data = []

        x, y = self.model.get_data()
        self.figure.add_trace(go.Scatter(x=x, y=y))
