import sys


class TextStatistics:
    """
    A class to hold statistics about a given text.

    Attributes:
        length (int): Total number of characters in the text.
        uppercase (int): Number of uppercase letters.
        lowercase (int): Number of lowercase letters.
        punctuation (int): Number of punctuation marks.
        spaces (int): Number of space characters.
        digits (int): Number of digit characters.
    """

    def __init__(
        self,
        length: int = 0,
        uppercase: int = 0,
        lowercase: int = 0,
        punctuation: int = 0,
        spaces: int = 0,
        digits: int = 0,
    ) -> None:
        """Initialize all counters to zero or to the supplied values."""
        self.length = length
        self.uppercase = uppercase
        self.lowercase = lowercase
        self.punctuation = punctuation
        self.spaces = spaces
        self.digits = digits


def count(text: str) -> TextStatistics:
    """
    Count various statistics in the given text.

    Args:
        text (str): The input text to analyze.

    Returns:
        TextStatistics: An object containing counts of various character types.
    """
    stats = TextStatistics(
        length=len(text),
    )

    for char in text:
        if char.isupper():
            stats.uppercase += 1
        elif char.islower():
            stats.lowercase += 1
        elif char.isspace():
            stats.spaces += 1
        elif char.isdigit():
            stats.digits += 1
        elif not char.isalnum():
            stats.punctuation += 1
    return stats


def main() -> None:
    """
    Main function to handle text statistics counting.

    Prints the following statistics:
    - Total number of characters
    - Number of uppercase letters
    - Number of lowercase letters
    - Number of punctuation marks
    - Number of spaces
    - Number of digits

    Raises:
        AssertionError: If more than one argument is provided.
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            text = ""
            try:
                text = input("What is the text to count?\n")
                text += "\n"
            except EOFError:
                pass

        f = count(text)

        print(f"The text contains {f.length} characters:")
        print(f"{f.uppercase} upper letters")
        print(f"{f.lowercase} lower letters")
        print(f"{f.punctuation} punctuation marks")
        print(f"{f.spaces} spaces")
        print(f"{f.digits} digits")
    except AssertionError as e:
        print(f"AssertionError: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
