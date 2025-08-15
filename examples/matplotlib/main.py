"""Runs the Matplotlib example."""

from examples.matplotlib.view import App


def main() -> None:
    app = App()
    app.server.start(open_browser=False)


if __name__ == "__main__":
    main()
