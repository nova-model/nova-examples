"""Test running all examples."""

import importlib
import os
from functools import partial
from multiprocessing import Process
from pathlib import Path
from time import sleep
from typing import List

import pytest
from requests import get

EXAMPLES_DIRECTORY = Path("examples")
ORNL_SUBDIRECTORY = Path("ornl")


def get_examples(directory: Path) -> List[str]:
    found_examples = []

    try:
        for example in sorted(os.listdir(directory)):
            if example.startswith(".") or example.startswith("_"):
                continue

            if example.startswith(str(ORNL_SUBDIRECTORY)):
                if not os.environ.get("INCLUDE_ORNL_TESTS", False):
                    continue

                found_examples.extend(get_examples(directory / ORNL_SUBDIRECTORY))
            elif os.path.isdir(directory / example):
                found_examples.append(example)
    except OSError:
        pass

    return found_examples


examples_list = get_examples(EXAMPLES_DIRECTORY)


def run_server(input_directory: str) -> None:
    example = importlib.import_module(f"examples.{input_directory}.main")
    example.main()


@pytest.mark.parametrize("input_directory", examples_list)
def test_example(input_directory: str) -> None:
    server_proc = Process(target=partial(run_server, input_directory))
    server_proc.start()

    sleep(5)

    try:
        response = get("http://localhost:8080/index.html")
        assert response.status_code == 200
    finally:
        server_proc.terminate()
