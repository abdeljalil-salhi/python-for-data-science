def give_bmi(
    height: list[int | float],
    weight: list[int | float],
) -> list[int | float]:
    """
    Calculate BMI values from lists of heights (in meters) and weights (in kg).
    BMI = weight / (height ** 2)

    Args:
        height (list of int or float): List of heights in meters.
        weight (list of int or float): List of weights in kilograms.

    Returns:
        list of int or float: List of calculated BMI values.
    """
    if not (isinstance(height, list) and isinstance(weight, list)):
        raise TypeError("height and weight must be lists")

    if len(height) != len(weight):
        raise ValueError("height and weight lists must have the same length")

    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError(
                "height and weight must contain " "only int or float values"
            )
        if h <= 0:
            raise ValueError("height must be greater than 0")

    bmi_list = [w / (h**2) for h, w in zip(height, weight)]

    return bmi_list


def apply_limit(
    bmi: list[int | float],
    limit: int,
) -> list[bool]:
    """
    Compare each BMI value against a specified limit.

    Args:
        bmi (list of int or float): List of BMI values.
        limit (int): The BMI limit to compare against.

    Returns:
        list of bool: List indicating if each BMI exceeds the limit.
    """
    if not isinstance(bmi, list):
        raise TypeError("bmi must be a list")

    if not isinstance(limit, int):
        raise TypeError("limit must be an integer")

    for value in bmi:
        if not isinstance(value, (int, float)):
            raise TypeError("bmi list must contain only int or float values")

    return [b > limit for b in bmi]
