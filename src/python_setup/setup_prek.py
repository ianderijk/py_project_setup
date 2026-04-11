from pathlib import Path
import subprocess
import os

CWD = Path(os.getcwd())


def get_contents() -> list[str]:
    with open(Path(__file__).parent / "prek_file_content.txt", "r") as file:
        return file.readlines()


def write_prek_toml(content: list[str]) -> None:
    with open(CWD / "prek.toml", "w") as file:
        for x in content:
            file.write(x)


def install_prek() -> None:
    os.chdir(CWD)
    subprocess.run(["prek", "install"])


def setup_prek() -> None:
    toml_file_contents = get_contents()
    write_prek_toml(toml_file_contents)
    install_prek()
