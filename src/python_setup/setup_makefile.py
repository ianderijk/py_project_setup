import os
from pathlib import Path

CWD = Path(os.getcwd())


def get_contents() -> list[str]:
    with open(Path(__file__).parent.parent.parent / "Makefile", "r") as file:
        return file.readlines()


def write_makefile(content: list[str]) -> None:
    with open(CWD / "Makefile", "w") as file:
        for x in content:
            file.write(x)


def create_makefile() -> None:
    contents = get_contents()
    write_makefile(contents)
