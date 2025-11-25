# NOVA Examples Repository

This repository contains examples of how to build application functionalities in the NOVA framework.

## List of Examples

1. [Creating a form for a Pydantic model](examples/pydantic_form)
    * `Validation`
2. [Using Pydantic to add options to a form field](examples/pydantic_form_with_options)
    * `Computed Fields`
3. [Create a JSON editor for a Pydantic model](examples/pydantic_monaco)
    * `Monaco Editor` `Validation`
4. [Conditionally rendering elements](examples/conditional_rendering)
    * `Conditions`
5. [Conditionally disabling elements](examples/conditional_disabling)
    * `Conditions`
6. [Creating a dialog](examples/dialog)
    * `Modals`
7. [Changing Pydantic rules based on user input](examples/dynamic_pydantic_rules)
    * `Validation`
8. [Complex Pydantic rules](examples/complex_pydantic_rules)
    * `Computed Fields` `Validation`
9. [Selecting datafiles from the server](examples/data_selector)
    * `Remote Data`
10. [Running a Galaxy tool](examples/run_galaxy_tool)
    * `Galaxy` `Asynchronous`
11. [Running a Galaxy workflow](examples/run_galaxy_workflow)
    * `Galaxy` `Asynchronous`
12. [Working with Plotly](examples/plotly)
    * `Visualization` `Plotting`
13. [Working with Matplotlib](examples/matplotlib)
    * `Visualization` `Plotting`
14. [Working with VTK](examples/vtk)
    * `Visualization` `Advanced Graphics`
15. [Synchronizing changes between tabs](examples/multitab)
    * `Events`

We also provide examples that take advantage of ORNL resources:

1. [Selecting datafiles from the Analysis Cluster](examples/ornl/neutron_data_selector)
    * `Remote Data`
2. [Selecting datafiles from ONCat](examples/ornl/oncat)
    * `Remote Data` `ONCat`

## Running Examples

If you want to run the examples, then you will need to install [Pixi](https://pixi.sh/latest/). Once done, run the following to run an example.

```bash
pixi install
pixi run python -m examples.{example_folder}
```

## Running Tests

This repo includes an automated test to ensure that each example runs:

```bash
pixi run pytest
```

You can set the environment variable `INCLUDE_ORNL_TESTS=1` if you want to test the examples that rely on specific ORNL resources. Note that you will need to run them from a location that has access to these resources.

## Example Structure

We use the MVVM framework for NOVA applications. With this in mind, each example is broken down into the following sections:

1. view - Sets up a Trame GUI for the example.
2. model - Sets up a Pydantic model and any business logic needed by the application.
3. view_model - Sets up a view model that binds the model and view.
4. main.py - Entrypoint for the Trame GUI.
