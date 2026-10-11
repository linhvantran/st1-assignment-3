"""Run the supplied demo or the Stage 9 interactive menu."""


import argparse

from smartcare.console import run_demo, run_menu


def main() -> None:
    """Run the demo, or report the intentionally incomplete interactive
    menu.
    """
    parser = argparse.ArgumentParser(
        description='SmartCare teaching application',
    )
    parser.add_argument('--interactive', action='store_true')
    args = parser.parse_args()
    if args.interactive:
        try:
            run_menu()
        except NotImplementedError as error:
            print(error)
    else:
        run_demo()
if __name__ == '__main__':
    main()
