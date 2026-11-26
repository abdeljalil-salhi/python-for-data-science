import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes a 2D list (array-like), prints its shape,
    slices it from start to end (row-wise), prints the new shape,
    and returns the sliced part as a regular Python list.

    Parameters:
        family: list of lists (2D array-like structure)
        start:  starting row index (inclusive)
        end:    ending row index (exclusive, like Python slicing)

    Returns:
        list: sliced 2D list (list of lists)
    """
    try:
        arr = np.array(family)
    except (TypeError, ValueError):
        raise TypeError("family must be a 2D list containing only numbers")

    if arr.ndim != 2:
        raise ValueError("family must be a 2D array (list of lists)")

    if not np.issubdtype(arr.dtype, np.number):
        raise TypeError("family must be a 2D list containing only numbers")

    rows, cols = arr.shape

    print(f"My shape is : ({rows}, {cols})")

    # Negative indices follow the usual Python slicing rules.
    if start < 0:
        start = max(rows + start, 0)
    if end < 0:
        end = max(rows + end, 0)

    if start > rows or end > rows:
        raise IndexError("start/end indices out of bounds")

    sliced = arr[start:end, :]

    new_rows, new_cols = sliced.shape
    print(f"My new shape is : ({new_rows}, {new_cols})")

    return sliced.tolist()
