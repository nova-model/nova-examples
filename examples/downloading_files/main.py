"""Runs the file download example."""

from examples.downloading_files.view import App


def main() -> None:
    app = App()
    app.server.start(open_browser=False)


if __name__ == "__main__":
    main()
