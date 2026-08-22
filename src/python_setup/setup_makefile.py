import os
from pathlib import Path

CWD = Path(os.getcwd())


def get_contents() -> list[str]:
    with open(Path(__file__).parent / "makefile_content.txt", "r") as file:
        return file.readlines()


def write_makefile(name: str, content: list[str]) -> None:
    with open(CWD / name / "Makefile", "w") as file:
        for x in content:
            file.write(x)


def create_makefile(name: str) -> None:
    contents = get_contents()
    write_makefile(name, contents)
