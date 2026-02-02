import sys


def main() -> None:
    if len(sys.argv) != 2:
        if len(sys.argv) == 1:
            sys.exit(0)
        else:
            raise AssertionError("more than one argument is provided")

    arg = sys.argv[1]

    try:
        number = int(arg)
    except ValueError:
        raise AssertionError("argument is not an integer")

    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}", file=sys.stderr)
        sys.exit(1)
