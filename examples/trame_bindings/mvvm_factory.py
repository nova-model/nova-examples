"""MVVM factory for setting up view model(s)."""

from nova.mvvm.interface import BindingInterface

from .model import Model
from .view_model import ViewModel


def create_vm(binding: BindingInterface) -> ViewModel:
    model = Model()
    view_model = ViewModel(model, binding)

    return view_model
