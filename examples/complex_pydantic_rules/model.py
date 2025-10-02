"""
Model implementation for complex Pydantic rules example.

Here, we will create a Pydantic rule to use nltk to clean and tokenize text provided by the user.
"""

import re

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from pydantic import BaseModel, Field, model_validator
from typing_extensions import Self


class FormData(BaseModel):
    """Pydantic model for the form data."""

    tokenized_text: str = Field(default="", title="Tokenized Text")
    text: str = Field(default="", title="Input Text")

    # Now, we will leverage Pydantic to clean and tokenize the text.
    # One could also use a Pydantic computed_field here.
    @model_validator(mode="after")
    def tokenize_text(self) -> Self:
        input_text = self.text.lower()

        # If any field in the model is invalid, then you can raise a ValueError and display the error to the user.
        if "error" in input_text:
            raise ValueError("Text must not contain the word error.")

        # Remove punctuation and other non-word text.
        cleaned_text = re.sub(r"[\W]", " ", input_text)

        # Tokenize the text and remove stopwords.
        words = word_tokenize(cleaned_text)
        stop_words = set(stopwords.words("english"))
        self.tokenized_text = " ".join([word for word in words if word not in stop_words])

        # This is required by Pydantic.
        return self


class Model:
    """Model implementation for complex Pydantic rules example."""

    def __init__(self) -> None:
        nltk.download("stopwords")
        nltk.download("punkt_tab")

        self.form = FormData()
