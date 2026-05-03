import argparse
from setup_uv import setup_uv
from setup_prek import setup_prek
from setup_dirs import create_project_directories
from setup_makefile import create_makefile


def main() -> None:
    parser = argparse.ArgumentParser(epilog="Project set up complete")
    parser.add_argument("mode", choices=["full", "uv", "prek"])
    args = parser.parse_args()

    if args.mode == "full":
        create_project_directories()
        setup_uv()
        setup_prek()
        create_makefile()
    elif args.mode == "uv":
        setup_uv()
    elif args.mode == "prek":
        setup_prek()


if __name__ == "__main__":
    main()
