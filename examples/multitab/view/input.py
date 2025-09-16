"""View for the input tab."""

from nova.trame.view.components import InputField
from nova.trame.view.layouts import GridLayout


class InputTab:
    """View for the input tab."""

    def __init__(self) -> None:
        self.create_ui()

    def create_ui(self) -> None:
        with GridLayout(columns=3, classes="mb-4", gap="0.5em"):
            InputField("inputs.count")
            InputField("inputs.min")
            InputField("inputs.max")
