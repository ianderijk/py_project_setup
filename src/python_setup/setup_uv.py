import subprocess
import os
from pathlib import Path

CWD = Path(os.getcwd())


def initialise_uv() -> None:
    os.chdir(CWD)
    subprocess.run(["uv", "init"])


def add_dependencies() -> None:
    os.chdir(CWD)
    subprocess.run(["uv", "sync"])


def read_toml_file() -> list[str]:
    with open(Path(__file__).parent.parent.parent / "pyproject.toml", "r") as file:
        return file.readlines()


def override_project_name(contents: list[str]) -> list[str]:
    edited_contents = []
    project_name = CWD.stem
    for x in contents:
        if "name = " in x:
            override = x.replace("python-setup", project_name)
            edited_contents.append(override)
            continue
        edited_contents.append(x)
    return edited_contents


def overwrite_toml_file(contents: list[str]) -> None:
    with open(CWD / "pyproject.toml", "w") as file:
        for x in contents:
            file.write(x)


def setup_uv() -> None:
    initialise_uv()
    contents = read_toml_file()
    contents = override_project_name(contents)
    overwrite_toml_file(contents)
    add_dependencies()
