import subprocess

def initialise_uv() -> None:
    subprocess.run(["uv", "init"])
