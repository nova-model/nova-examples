"""View model implementation for VTK example."""

from nova.mvvm.interface import BindingInterface
from vtkmodules.vtkRenderingCore import vtkActor

from .model import Model


class ViewModel:
    """View model implementation for VTK example."""

    def __init__(self, model: Model, binding: BindingInterface) -> None:
        self.model = model

    def get_actor(self) -> vtkActor:
        return self.model.get_actor()
