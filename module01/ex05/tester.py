import sys

from load_image import ft_load
from pimp_image import ft_blue, ft_green, ft_grey, ft_invert, ft_red


def main() -> None:
    """Apply every filter to the sample image and report load errors."""
    try:
        array = ft_load("landscape.jpg")
        print(array)
        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)
        print(ft_invert.__doc__)
    except (FileNotFoundError, ValueError, RuntimeError) as error:
        print(f"Unable to process image: {type(error).__name__} - {error}",
              file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
