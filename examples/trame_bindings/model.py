"""Model implementation for Trame bindings example."""

from pydantic import BaseModel, Field


class PydanticModel(BaseModel):
    """Pydantic model for Trame bindings example."""

    title: str = Field(default="", title="Title")
    button_clicks: int = Field(default=0)


class Model:
    """Model implementation for Trame bindings example."""

    def __init__(self) -> None:
        self.pydantic = PydanticModel()

    def get_title(self) -> str:
        return self.pydantic.title

    def increment_button_clicks(self) -> None:
        self.pydantic.button_clicks += 1
