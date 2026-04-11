import os
from pathlib import Path

CWD = Path(os.getcwd())


def create_project_name() -> str:
    dir_name = CWD.stem
    project_name = dir_name.lower().replace(" ", "-").replace("-", "_")
    return project_name


def create_project_directories() -> None:
    src_path = CWD / "src"
    os.mkdir(src_path)
    project_name = create_project_name()
    project_dir = src_path / project_name
    os.mkdir(project_dir)
    os.chdir(project_dir)
    with open("__init__.py", "w") as _:
        pass
