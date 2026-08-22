import subprocess
import os
from pathlib import Path

CWD = Path(os.getcwd())


def initialise_uv(name: str) -> None:
    os.chdir(CWD / name)
    subprocess.run(["uv", "init"])


def add_dependencies(name: str) -> None:
    os.chdir(CWD / name)
    subprocess.run(["uv", "sync"])
    subprocess.run(
        ["uv", "add", "--index-url", "http://192.168.0.29:8080/simple", "logger"]
    )


def read_toml_file() -> list[str]:
    with open(Path(__file__).parent / "pyproject_file_contents.txt", "r") as file:
        return file.readlines()


def override_project_name(contents: list[str]) -> list[str]:
    edited_contents = []
    project_name = CWD.stem
    for x in contents:
        if "name = " in x:
            override = x.replace("project", project_name)
            edited_contents.append(override)
            continue
        edited_contents.append(x)
    return edited_contents


def overwrite_toml_file(name: str, contents: list[str]) -> None:
    with open(CWD / name / "pyproject.toml", "w") as file:
        for x in contents:
            file.write(x)


def setup_uv(name: str) -> None:
    initialise_uv(name)
    contents = read_toml_file()
    contents = override_project_name(contents)
    overwrite_toml_file(name, contents)
    add_dependencies(name)
