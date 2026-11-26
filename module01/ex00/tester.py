import sys

from give_bmi import apply_limit, give_bmi


def main() -> None:
    """Run the provided example and report invalid input cleanly."""
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    try:
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except (TypeError, ValueError) as error:
        print(f"Invalid input: {type(error).__name__} - {error}",
              file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
