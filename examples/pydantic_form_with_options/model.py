"""Model implementation for Pydantic form with options example."""

from enum import Enum
from typing import Dict, List

from pydantic import BaseModel, Field

DEFAULT_ORGS = ["Academia", "Government", "Industry"]
EXTRA_ORGS = ["Non-Profit", "Independent"]


class CountryCodes(str, Enum):
    """Enumeration for telephone country codes."""

    australia = "+61 (Australia)"
    north_america = "+1 (US & Canada)"
    united_kingdom = "+44 (United Kingdom)"


class FormData(BaseModel):
    """Pydantic model for the form data."""

    phone_number: str = Field(default="", title="Phone Number")

    # This represents a static list of options for the user. It must use an Enum-based type in order for NOVA to
    # automatically populate the options in the GUI.
    phone_country: CountryCodes = Field(default=CountryCodes.north_america, title="Country Code")

    show_all_org_options: bool = Field(default=False, title="Show All?")
    organization: str = Field(default="", title="Organization")

    # This represents a dynamic list of options for the user. In this case, you will need to manually declare the list
    # of options in the GUI.
    org_options: List[Dict[str, str]] = Field(default=[])


class Model:
    """Model implementation for Pydantic form with options example."""

    def __init__(self) -> None:
        self.form = FormData()
        self.update_org_options()

    def update_org_options(self) -> None:
        if self.form.show_all_org_options:
            orgs = DEFAULT_ORGS + EXTRA_ORGS
        else:
            orgs = DEFAULT_ORGS

        # For radio button groups, a dictionary with title and value keys for each item in the dynamic list is required.
        self.form.org_options = [{"title": org, "value": org} for org in orgs]
