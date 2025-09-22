"""Runs the NDIP workflow example."""

from examples.run_ndip_workflow.view import App


def main() -> None:
    app = App()
    app.server.start(open_browser=False)


if __name__ == "__main__":
    main()
