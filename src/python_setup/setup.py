import argparse
from setup_uv import initialise_uv
from setup_prek import setup_prek
from setup_dirs import create_project_directories


def main() -> None:
    parser = argparse.ArgumentParser(epilog="Project set up complete")
    parser.add_argument("mode", choices=["full", "uv", "prek"])
    args = parser.parse_args()

    if args.mode == "full":
        initialise_uv()
        setup_prek()
        create_project_directories()
    elif args.mode == "uv":
        initialise_uv()
    elif args.mode == "prek":
        setup_prek()


if __name__ == "__main__":
    main()
