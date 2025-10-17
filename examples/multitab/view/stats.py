"""View for the stats tab."""

from typing import Any

from nova.trame.view.components import InputField
from nova.trame.view.layouts import GridLayout, VBoxLayout
from trame.widgets import html


class StatsTab:
    """View for the stats tab."""

    def __init__(self, **kwargs: Any) -> None:
        self.create_ui(**kwargs)

    def create_ui(self, **kwargs: Any) -> None:
        with VBoxLayout(**kwargs):
            html.P("Generated List: {{ stats.values }}", classes="mb-4")

            with GridLayout(columns=3, gap="0.5em"):
                InputField("stats.average", readonly=True)
                InputField("stats.mean", readonly=True)
                InputField("stats.median", readonly=True)
                InputField("stats.quantile", readonly=True)
                InputField("stats.std", readonly=True)
                InputField("stats.variance", readonly=True)
