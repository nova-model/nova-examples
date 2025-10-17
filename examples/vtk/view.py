"""View for VTK example."""

import vtkmodules.vtkRenderingOpenGL2  # noqa
from nova.mvvm.trame_binding import TrameBinding
from nova.trame import ThemedApp
from nova.trame.view.layouts import VBoxLayout
from trame.widgets import vtk

# VTK factory initialization
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleSwitch  # noqa
from vtkmodules.vtkRenderingCore import vtkRenderer, vtkRenderWindow, vtkRenderWindowInteractor

from .model import Model
from .view_model import ViewModel


class App(ThemedApp):
    """View for VTK example."""

    def __init__(self) -> None:
        super().__init__()

        self.create_vm()

        self.create_renderer()
        self.create_ui()

    def create_renderer(self) -> None:
        renderer = vtkRenderer()
        self.render_window = vtkRenderWindow()
        self.render_window.AddRenderer(renderer)
        self.render_window.OffScreenRenderingOn()  # Prevent popup window

        render_window_interactor = vtkRenderWindowInteractor()
        render_window_interactor.SetRenderWindow(self.render_window)
        render_window_interactor.GetInteractorStyle().SetCurrentStyleToTrackballCamera()

        renderer.AddActor(self.view_model.get_actor())
        renderer.ResetCamera()
        self.render_window.Render()

    def create_ui(self) -> None:
        with super().create_ui() as layout:
            with layout.content:
                with VBoxLayout(gap="0.5em", stretch=True):
                    # Choosing vtkRemoteView will enforce server-side rendering. We strongly recommend this for
                    # anything non-trivial in size.
                    vtk.VtkRemoteView(self.render_window)

    def create_vm(self) -> None:
        binding = TrameBinding(self.state)

        model = Model()
        self.view_model = ViewModel(model, binding)
