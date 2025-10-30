# NOVA Examples Repository

This repository contains examples of how to build application functionalities in the NOVA framework.

## List of Examples

1. [Creating a form for a Pydantic model](examples/pydantic_form)
2. [Create a JSON editor for a Pydantic model](examples/pydantic_monaco)
3. [Conditionally rendering elements](examples/conditional_rendering)
4. [Conditionally disabling elements](examples/conditional_disabling)
5. [Creating a dialog](examples/dialog)
6. [Changing Pydantic rules based on user input](examples/dynamic_pydantic_rules)
7. [Complex Pydantic rules](examples/complex_pydantic_rules)
8. [Selecting datafiles from the server](examples/data_selector)
9. [Running a Galaxy tool](examples/run_galaxy_tool)
10. [Running a Galaxy workflow](examples/run_galaxy_workflow)
11. [Working with Plotly](examples/plotly)
12. [Working with Matplotlib](examples/matplotlib)
13. [Working with VTK](examples/vtk)
14. [Synchronizing changes between tabs](examples/multitab)

We also provide examples that take advantage of ORNL resources:

1. [Selecting datafiles from the Analysis Cluster](examples/ornl/neutron_data_selector)
2. [Selecting datafiles from ONCat](examples/ornl/oncat)

## Running Examples

If you want to run the examples, then you will need to install [Poetry](https://python-poetry.org/). Once done, run the following to run an example.

```bash
poetry install
poetry run python examples/{example_folder}/main.py
```

## Running Tests

This repo includes an automated test to ensure that each example runs:

```bash
poetry install
poetry run pytest
```

You can set the environment variable `INCLUDE_ORNL_TESTS=1` if you want to test the examples that rely on specific ORNL resources. Note that you will need to run them from a location that has access to these resources.

## Example Structure

We use the MVVM framework for NOVA applications. With this in mind, each example is broken down into the following sections:

1. view - Sets up a Trame GUI for the example.
2. model - Sets up a Pydantic model and any business logic needed by the application.
3. view_model - Sets up a view model that binds the model and view.
4. main.py - Entrypoint for the Trame GUI.
