"""Model implementation for Pydantic/Monaco example."""

from typing import Any, Dict

from pydantic import BaseModel, Field


class FormData(BaseModel):
    """Pydantic model definition."""

    input_file: str = Field(default="test.txt", min_length=1)
    run_number: int = Field(default=1, gt=0)
    use_parameter_x: bool = Field(default=False)
    use_parameter_y: bool = Field(default=False)
    use_parameter_z: bool = Field(default=False)
    advanced_settings: Dict[str, Any] = Field(
        default={"advanced_setting_x": False, "advanced_setting_y": 0, "advanced_setting_z": "test"}
    )


class Model:
    """Model implementation for Pydantic/Monaco example."""

    def __init__(self) -> None:
        self.form = FormData()

    def set_from_json(self, json_data: str) -> None:
        self.form = FormData.model_validate_json(json_data)
