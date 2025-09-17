"""Runs the dynamic Pydantic rules example."""

from examples.dynamic_pydantic_rules.view import App


def main() -> None:
    app = App()
    app.server.start(open_browser=False)


if __name__ == "__main__":
    main()
