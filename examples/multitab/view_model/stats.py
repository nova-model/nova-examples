"""View model for the stats tab."""

from typing import Any, List, Optional

from nova.common.events import get_event
from nova.mvvm.interface import BindingInterface

from ..model.stats import StatsModel


class StatsViewModel:
    """View model for the stats tab."""

    def __init__(self, model: StatsModel, binding: BindingInterface) -> None:
        self.model = model

        self.stats_bind = binding.new_bind(self.model.stats)

        # To listen to an event sent from other view models, we can call connect.
        self.update_event = get_event("inputs_updated")
        self.update_event.connect(self.on_inputs_update)

    def on_inputs_update(self, sender: Any = None, values: Optional[List[int]] = None, **kwargs: Any):
        self.model.update(values)
        self.stats_bind.update_in_view(self.model.stats)
