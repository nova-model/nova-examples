"""Model implementation for Plotly example."""

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
    """Model implementation for Plotly example."""

    def __init__(self) -> None:
        self.plot_data = PlotData()

    def get_data(self) -> np.ndarray:
        domain = np.arange(self.plot_data.data_points)
        data = np.radians(np.mod(domain, 360))

        match self.plot_data.function:
            case FunctionOptions.cosine:
                return domain, np.cos(data)
            case FunctionOptions.sine:
                return domain, np.sin(data)

        return domain, data
