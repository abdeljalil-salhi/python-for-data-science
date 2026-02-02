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
        arr = np.array(family, dtype=float)
    except Exception:
        raise TypeError("family must be a 2D list containing only numbers")

    if arr.ndim != 2:
        raise ValueError("family must be a 2D array (list of lists)")

    rows, cols = arr.shape

    print(f"My shape is : ({rows}, {cols})")

    # negative indices (like normal array slicing)
    if end < 0:
        end = rows + end

    if start < 0 or end < 0 or start > rows or end > rows:
        raise IndexError("start/end indices out of bounds")

    if start >= end:
        sliced = arr[start:end]
        print(f"My new shape is : ({sliced.shape[0]}, {cols})")
        return sliced.tolist()

    sliced = arr[start:end, :]

    new_rows, new_cols = sliced.shape
    print(f"My new shape is : ({new_rows}, {new_cols})")

    return sliced.tolist()
