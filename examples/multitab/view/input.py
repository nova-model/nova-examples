"""View for the input tab."""

from typing import Any

from nova.trame.view.components import InputField
from nova.trame.view.layouts import GridLayout


class InputTab:
    """View for the input tab."""

    def __init__(self, **kwargs: Any) -> None:
        self.create_ui(**kwargs)

    def create_ui(self, **kwargs: Any) -> None:
        with GridLayout(columns=3, classes="mb-4", gap="0.5em", **kwargs):
            InputField("inputs.count")
            InputField("inputs.min")
            InputField("inputs.max")
