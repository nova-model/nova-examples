"""Model implementation for Pydantic/Monaco example."""

from enum import Enum

import numpy as np
from pydantic import BaseModel, Field


class FunctionOptions(str, Enum):
    """Enum defining a list of options for a Pydantic field."""

    cosine = "cos"
    sine = "sin"


class PlotData(BaseModel):
    """Pydantic model definition."""

    data_points: int = Field(default=0, ge=0, title="Number of Data Points")
    function: FunctionOptions = Field(default=FunctionOptions.cosine, title="Function")


class Model:
    """Model implementation for Matplotlib example."""

    def __init__(self) -> None:
        self.plot_data = PlotData()

    def get_data(self) -> np.ndarray:
        data = np.radians(np.mod(np.arange(self.plot_data.data_points), 360))

        match self.plot_data.function:
            case FunctionOptions.cosine:
                return np.cos(data)
            case FunctionOptions.sine:
                return np.sin(data)

        return data
