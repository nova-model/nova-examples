"""Model implementation for Pydantic form example."""

from pydantic import BaseModel, Field, computed_field, field_validator


class FormData(BaseModel):
    """Pydantic model for the form data."""

    user_name: str = Field(default="", title="User Name")
    domain_name: str = Field(default="", title="Domain Name")

    @computed_field
    @property
    def email(self) -> str:
        if not self.user_name or not self.domain_name:
            return ""
        return f"{self.user_name}@{self.domain_name}"

    @field_validator("domain_name", mode="after")
    @classmethod
    def validate_domain_name(cls, value: str) -> str:
        if value and "." not in value:
            raise ValueError("Invalid domain name.")

        return value


class Model:
    """Model implementation for Pydantic form example."""

    def __init__(self) -> None:
        self.form = FormData()
