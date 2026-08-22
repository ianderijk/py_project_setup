import os
from pathlib import Path

CWD = Path(os.getcwd())


def create_project_name(name: str) -> str:
    project_name = name.lower().replace(" ", "-").replace("-", "_")
    return project_name


def create_project_directories(name: str) -> None:
    src_path = CWD / name / "src"
    os.mkdir(src_path)
    project_name = create_project_name(name)
    project_dir = src_path / project_name
    os.mkdir(project_dir)
    os.chdir(project_dir)
    with open("__init__.py", "w") as _:
        pass
