# NOVA Examples Repository

This repository contains examples of how to build application functionalities in the NOVA framework.

## List of Examples

1. [Creating a form for a Pydantic model](examples/pydantic_form)
2. [Create a JSON editor for a Pydantic model](examples/pydantic_monaco)
3. [Conditionally rendering elements](examples/conditional_rendering)
4. [Conditionally disabling elements](examples/conditional_disabling)
5. [Changing Pydantic rules based on user input](examples/dynamic_pydantic_rules)
6. [Complex Pydantic rules](examples/complex_pydantic_rules)
7. [Working with Plotly](examples/plotly)
8. [Working with Matplotlib](examples/matplotlib)
9. [Synchronizing changes between tabs](examples/multitab)

## Running Examples

If you want to run the examples, then you will need to install [Poetry](https://python-poetry.org/). Once done, run the following to run an example.

```bash
poetry install
poetry run python examples/{example_folder}/main.py
```

## Example Structure

We use the MVVM framework for NOVA applications. With this in mind, each example is broken down into the following sections:

1. view - Sets up a Trame GUI for the example.
2. model - Sets up a Pydantic model and any business logic needed by the application.
3. view_model - Sets up a view model that binds the model and view.
4. main.py - Entrypoint for the Trame GUI.
