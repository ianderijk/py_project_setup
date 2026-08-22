import typer
import os
from pathlib import Path
from .setup_uv import setup_uv
from .setup_prek import setup_prek
from .setup_dirs import create_project_directories
from .setup_makefile import create_makefile


app = typer.Typer(help="Python project setup")


@app.command()
def pyproject(name: str):
    cwd = Path(os.getcwd())
    project_path = cwd / name
    if not project_path.exists():
        os.mkdir(project_path)
    os.chdir(project_path)
    create_project_directories(name)
    setup_uv(name)
    setup_prek(name)
    create_makefile(name)


if __name__ == "__main__":
    app()
