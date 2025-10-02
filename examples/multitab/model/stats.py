"""Model for stats tab."""

from typing import List, Optional

import numpy as np
from pydantic import BaseModel, Field


class StatsFields(BaseModel):
    """Pydantic class for stats tab."""

    average: Optional[float] = Field(default=None, title="Average")
    mean: Optional[float] = Field(default=None, title="Mean")
    median: Optional[float] = Field(default=None, title="Median")
    quantile: Optional[float] = Field(default=None, title="75th Percentile")
    std: Optional[float] = Field(default=None, title="Standard Deviation")
    variance: Optional[float] = Field(default=None, title="Variance")
    values: List[int] = Field(default=[])


class StatsModel:
    """Model for stats tab."""

    def __init__(self) -> None:
        self.stats = StatsFields()

    def update(self, values: List[int]) -> None:
        self.stats.values = values

        self.stats.average = np.average(self.stats.values)
        self.stats.mean = np.mean(self.stats.values)
        self.stats.median = np.median(self.stats.values)
        self.stats.quantile = np.quantile(self.stats.values, 0.75)
        self.stats.std = np.std(self.stats.values)
        self.stats.variance = np.var(self.stats.values)
