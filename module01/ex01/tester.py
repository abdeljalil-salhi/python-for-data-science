import sys

from array2D import slice_me


def main() -> None:
    """Run the provided slicing examples with clean error reporting."""
    family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
    try:
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except (TypeError, ValueError, IndexError) as error:
        print(f"Invalid input: {type(error).__name__} - {error}",
              file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
