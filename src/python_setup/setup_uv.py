import subprocess
import os
from pathlib import Path

CWD = Path(os.getcwd())


def initialise_uv() -> None:
    os.chdir(CWD)
    subprocess.run(["uv", "init"])
