"""Runs the Pydantic form example."""

from examples.pydantic_form.view import App


def main() -> None:
    app = App()
    app.server.start(open_browser=False)


if __name__ == "__main__":
    main()
