"""Model implementation for VTK example."""

from vtkmodules.vtkFiltersSources import vtkConeSource
from vtkmodules.vtkRenderingCore import vtkActor, vtkPolyDataMapper


class Model:
    """Model implementation for Plotly example."""

    def __init__(self) -> None:
        pass

    def get_actor(self) -> vtkActor:
        cone_source = vtkConeSource()
        cone_source.SetResolution(10)

        mapper = vtkPolyDataMapper()
        actor = vtkActor()
        mapper.SetInputConnection(cone_source.GetOutputPort())
        actor.SetMapper(mapper)

        return actor
