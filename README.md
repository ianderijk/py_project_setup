# Project

Automating the setup of new python projects.

## Includes

- Initialising the directory structure as below:
```
- project/
  - .gitignore
  - .python-version
  - Makefile
  - main.py
  - prek.toml
  - pyproject.toml
  - README.md
  - uv.lock
  - src/
    - project/
      - __init__.py
```
- Project initialisation is handled by `uv`
- Prek initialised with setup detailed in `src/python_setup/prek_file_contents.txt`
- Standard project Makefile created
- pyproject.toml file updated with the project name and additions detailed in `src/python_setup/pyproject_file_contents.txt`
- An empty `__init__.py` file in the project directory


## Use

The project can be build and installed globally using uv and the command `make tool`. When built and installed running `pyproj <project-name>`
