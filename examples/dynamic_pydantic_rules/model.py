"""Model implementation for dynamic Pydantic rules example."""

from pydantic import BaseModel, Field, model_validator
from typing_extensions import Self


class FormData(BaseModel):
    """Pydantic model for the form data."""

    min: float = Field(default=0.0, title="Minimum")
    max: float = Field(default=10.0, title="Maximum")
    value: float = Field(default=5.0, title="Value")

    @model_validator(mode="after")
    def validate_value_in_range(self) -> Self:
        if self.value < self.min or self.value > self.max:
            raise ValueError("Value must be between Minimum and Maximum")

        return self


class Model:
    """Model implementation for dynamic Pydantic rules example."""

    def __init__(self) -> None:
        self.form = FormData()
