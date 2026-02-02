import sys


NESTED_MORSE = {
    " ": "/ ", "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ", "E": ". ",
    "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ", "J": ".--- ",
    "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ", "O": "--- ",
    "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
    "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ", "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ", "4": "....- ",
    "5": "..... ", "6": "-.... ", "7": "--... ", "8": "---.. ", "9": "----. "
}


def main() -> None:
    """
    Convert input string to Morse code or show error.

    Raises:
        AssertionError: If the input arguments are invalid.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]
        if not isinstance(text, str):
            raise AssertionError("the arguments are bad")

        result = "".join(
            NESTED_MORSE.get(c.upper(), "#")
            for c in text
        ).rstrip()

        if "#" in result:
            raise AssertionError("the arguments are bad")

        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
