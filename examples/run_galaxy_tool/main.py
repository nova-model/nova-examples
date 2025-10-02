"""Runs the Galaxy tool example."""

from examples.run_galaxy_tool.view import App


def main() -> None:
    app = App()
    app.server.start(open_browser=False)


if __name__ == "__main__":
    main()
