"""Model implementation for Galaxy tool example."""

from enum import Enum
from io import BytesIO
from typing import List, Tuple

from nova.galaxy import Parameters, Tool
from nova.galaxy.interfaces import BasicTool
from PIL import Image
from PIL.ImageStat import Stat
from pydantic import BaseModel, Field


class FractalOptions(str, Enum):
    """Defines options for the fractal_type field."""

    mandelbrot = "Mandelbrot Set"
    julia = "Julia Set Animation"
    random = "Random Walk"
    markus = "Markus-Lyapunov Fractal"


class FormData(BaseModel):
    """Pydantic model for the form data."""

    fractal_type: FractalOptions = Field(default=FractalOptions.mandelbrot, title="Type")


class ImageStatistics(BaseModel):
    """Pydantic model for holding image statistics."""

    count: List[int] = Field(default=[])
    extrema: List[Tuple[int, int]] = Field(default=[])
    mean: List[float] = Field(default=[])
    median: List[int] = Field(default=[])


class Model:
    """Model implementation for Galaxy tool example."""

    def __init__(self) -> None:
        self.form = FormData()
        self.stats = ImageStatistics()


class FractalsTool(BasicTool):
    """Class that prepares IPS Fastran tool."""

    def __init__(self, model: Model) -> None:
        super().__init__()
        self.model = model

    def prepare_tool(self) -> Tuple[Tool, Parameters]:
        # Pass the fractal type dropdown value to the tool. The "option" name comes from the tool XML file.
        tool_params = Parameters()
        tool_params.add_input(name="option", value=self.model.form.fractal_type)

        # Create the tool.
        self.tool = Tool(id="neutrons_fractal")

        return self.tool, tool_params

    def compute_stats(self) -> None:
        outputs = self.tool.get_results()
        output = outputs.get_dataset("output").get_content()

        img = Image.open(BytesIO(output))
        stat = Stat(img)

        self.model.stats.count = stat.count
        self.model.stats.extrema = stat.extrema
        self.model.stats.mean = [round(mean, 3) for mean in stat.mean]
        self.model.stats.median = stat.median

    def get_results(self, tool: Tool) -> None:
        pass
