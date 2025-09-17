"""Model implementation for conditional disabling example."""

from pydantic import BaseModel, Field


class FormData(BaseModel):
    """Pydantic model for the form data."""

    disable_phone_field: bool = Field(default=False, title="Disable Phone Number?")
    email_address: str = Field(default="", title="Email Address")
    full_name: str = Field(default="", title="Full Name")
    phone_number: str = Field(default="", title="Phone Number")


class Model:
    """Model implementation for conditional disabling example."""

    def __init__(self) -> None:
        self.form = FormData()
