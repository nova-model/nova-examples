"""Model for input tab."""

from typing import List

import numpy as np
from pydantic import BaseModel, Field, model_validator
from typing_extensions import Self


class InputFields(BaseModel):
    """Pydantic class for input tab."""

    count: int = Field(default=1, ge=1, title="Count")
    min: int = Field(default=0, title="Minimum")
    max: int = Field(default=10, title="Maximum")

    @model_validator(mode="after")
    def validate_range(self) -> Self:
        if self.max < self.min:
            raise ValueError("The maximum must be greater than or equal to the minimum.")

        return self


class InputModel:
    """Model for input tab."""

    def __init__(self) -> None:
        self.inputs = InputFields()

    def get_values(self) -> List[int]:
        return np.random.randint(
            low=int(self.inputs.min), high=int(self.inputs.max) + 1, size=int(self.inputs.count)
        ).tolist()
