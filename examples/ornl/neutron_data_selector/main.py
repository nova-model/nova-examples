"""Runs the neutron data selector example."""

from examples.ornl.neutron_data_selector.view import App


def main() -> None:
    app = App()
    app.server.start(open_browser=False)


if __name__ == "__main__":
    main()
