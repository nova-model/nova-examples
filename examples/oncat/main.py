"""Runs the ONCat example."""

from examples.oncat.view import App


def main() -> None:
    app = App()
    app.server.start(open_browser=False)


if __name__ == "__main__":
    main()
