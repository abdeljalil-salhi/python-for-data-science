import sys


def parse_arguments() -> tuple[str, int]:
    """
    Parse command line arguments and validate them.

    Returns:
        tuple[str, int]: A tuple containing the string S and integer N

    Raises:
        AssertionError: if number of arguments or types are incorrect
    """
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")

    s_arg, n_arg = sys.argv[1], sys.argv[2]

    if not isinstance(s_arg, str):
        raise AssertionError("the arguments are bad")

    try:
        n = int(n_arg)
    except ValueError:
        raise AssertionError("the arguments are bad")

    return s_arg, n


def main() -> None:
    """
    Main program logic:
    - Takes a string S and integer N as arguments
    - Returns list of words from S longer than N characters
    - Uses list comprehension + lambda

    Raises:
        AssertionError: if arguments are invalid
    """
    try:
        text, threshold = parse_arguments()

        words = text.split()

        result = [word for word in words
                  if (lambda w: len(w) > threshold)(word)]

        print(result)

    except AssertionError as e:
        print(f"AssertionError: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
