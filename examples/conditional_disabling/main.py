"""Runs the conditional disabling example."""

from examples.conditional_disabling.view import App


def main() -> None:
    app = App()
    app.server.start(open_browser=False)


if __name__ == "__main__":
    main()
