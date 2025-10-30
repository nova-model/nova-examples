"""Runs the Pydantic form with options example."""

from examples.pydantic_form_with_options.view import App


def main() -> None:
    app = App()
    app.server.start(open_browser=False)


if __name__ == "__main__":
    main()
