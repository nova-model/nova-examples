# NOVA Examples Repository

This repository contains examples of how to build application functionalities in the NOVA framework.

## Running Examples

If you want to run the examples, then you will need to install [Poetry](https://python-poetry.org/). Once done, run the following to run an example.

```bash
poetry install
poetry run python examples/{example_folder}/main.py
```

## Example Structure

We use the MVVM framework for NOVA applications. With this in mind, each example is broken down into the following files:

1. view.py - Sets up a Trame GUI for the example.
2. model.py - Sets up a Pydantic model and any business logic needed by the application.
3. view_model.py - Sets up a view model that binds the model and view.
4. main.py - Entrypoint for the Trame GUI.

## List of Examples

1. [Creating a form for a Pydantic model](examples/pydantic_form)
