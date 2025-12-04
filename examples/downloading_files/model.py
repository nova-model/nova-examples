"""Model implementation for file download example."""

from typing import List

from pydantic import BaseModel, Field


class FormData(BaseModel):
    """Pydantic model for the form data."""

    selected_files: List[str] = Field(default=[], title="Selected Files")


class Model:
    """Model implementation for file download example."""

    def __init__(self) -> None:
        self.form = FormData()

    def get_selected_files(self) -> List[str]:
        return self.form.selected_files
