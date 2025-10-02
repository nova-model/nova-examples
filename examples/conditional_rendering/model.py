"""Model implementation for conditional rendering example."""

from pydantic import BaseModel, Field


class FormData(BaseModel):
    """Pydantic model for the form data."""

    comments: str = Field(default="", title="Comments")
    email_address: str = Field(default="", title="Email Address")
    full_name: str = Field(default="", title="Full Name")
    phone_number: str = Field(default="", title="Phone Number")
    show_phone_field: bool = Field(default=False, title="Add Phone Number?")
    show_comments_field: bool = Field(default=False)


class Model:
    """Model implementation for conditional rendering example."""

    def __init__(self) -> None:
        self.form = FormData()

    def toggle_comments(self) -> None:
        self.form.show_comments_field = not self.form.show_comments_field
