import sys
import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """
    Loads a CSV file using pandas and prints its dimensions.

    Args:
        path (str): Path to the CSV file

    Returns:
        pd.DataFrame | None: The loaded dataset or None if loading failed
    """
    try:
        df = pd.read_csv(path)

        rows, cols = df.shape
        print(f"Loading dataset of dimensions ({rows}, {cols})")

        return df

    except FileNotFoundError:
        print(f"Error: File '{path}' not found.", file=sys.stderr)
        return None

    except pd.errors.EmptyDataError:
        print(f"Error: File '{path}' is empty.", file=sys.stderr)
        return None

    except pd.errors.ParserError:
        print(
            f"Error: Unable to parse '{path}' — invalid CSV format.",
            file=sys.stderr,
        )
        return None

    except Exception as e:
        print(
            f"Unexpected error while loading '{path}': \
                {type(e).__name__} - {e}",
            file=sys.stderr,
        )
        return None
