"""Test running all examples."""

import importlib
import os
from functools import partial
from multiprocessing import Process
from pathlib import Path
from time import sleep

import pytest
from requests import get

base_path = Path("examples")
examples_list = []
try:
    for example in sorted(os.listdir(base_path)):
        if example.startswith(".") or example.startswith("_"):
            continue

        if os.path.isdir(base_path / example):
            examples_list.append(example)
except OSError:
    pass


def run_server(input_directory: str) -> None:
    example = importlib.import_module(f"examples.{input_directory}.main")
    example.main()


@pytest.mark.parametrize("input_directory", examples_list)
def test_example(input_directory: str) -> None:
    # The ONCat and NDIP examples can't run in GitHub CI, so we exclude them from the tests.
    if input_directory == "oncat" or "ndip" in input_directory:
        return

    server_proc = Process(target=partial(run_server, input_directory))
    server_proc.start()

    sleep(5)

    try:
        response = get("http://localhost:8080/index.html")
        assert response.status_code == 200
    finally:
        server_proc.terminate()
