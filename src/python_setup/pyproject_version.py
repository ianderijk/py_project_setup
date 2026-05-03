import requests
from pathlib import Path
from typing import NamedTuple

version = NamedTuple("version", [("semantic", str), ("numeric", float)])


def extract_version_num(package_version_text: str, project_name: str) -> version:
    # package version text includes examples such as "/packages/logwriter-1.0.0-py3-none-any.whl#sha25..."
    # so we need to slice the string between the project name and the py3 string
    package_semantic = (
        package_version_text[
            package_version_text.index(project_name)
            + len(project_name) : package_version_text.index("py3")
        ]
        .replace('"', "")
        .replace("-", "")
    )
    package_numeric_text = "".join([x for x in package_semantic if x.isnumeric()])
    package_numeric = float(package_numeric_text)
    package_version = version(package_semantic, package_numeric)
    return package_version


def find_published_versions(project_name: str) -> list[version]:
    response = requests.get(f"http://192.168.0.29:8080/simple/{project_name}/")
    response_text = response.text
    links_body = response_text[response_text.index("</h1>") + 5 :]
    links_text = links_body.split("<br>")
    wheels = [x for x in links_text if "any.whl" in x]
    package_versions = []
    for x in wheels:
        package_version = extract_version_num(x, project_name)
        package_versions.append(package_version)
    return package_versions


def find_toml_version() -> version:
    toml_path = Path(__file__).parent.parent.parent / "pyproject.toml"
    with open(toml_path, "r") as file:
        contents = file.readlines()
        for x in contents:
            if "version" in x:
                packcage_semantic = x[x.index('"') + 1 : x.rfind('"')]
                package_numeric = float(packcage_semantic.replace(".", ""))
                return version(packcage_semantic, package_numeric)
    raise Exception("Failed to find version record in pyproject.toml file")


def is_valid_publishing_version(project_name: str) -> bool:
    published_versions = find_published_versions(project_name)
    toml_version = find_toml_version()
    if max([x.numeric for x in published_versions]) >= toml_version.numeric:
        return False
    return True
