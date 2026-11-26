import sys

from load_image import ft_load


def main() -> None:
    """Load the sample image and report loading errors cleanly."""
    try:
        print(ft_load("landscape.jpg"))
    except (FileNotFoundError, ValueError, RuntimeError) as error:
        print(f"Unable to load image: {type(error).__name__} - {error}",
              file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
