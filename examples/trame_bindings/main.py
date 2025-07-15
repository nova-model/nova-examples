"""Runs the Trame bindings example."""

from examples.trame_bindings.view import App


def main() -> None:
    app = App()
    app.server.start(open_browser=False)


if __name__ == "__main__":
    main()
