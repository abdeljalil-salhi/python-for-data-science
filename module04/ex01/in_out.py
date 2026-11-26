def square(x: int | float) -> int | float:
    """Return the square of x."""
    return x * x


def pow(x: int | float) -> int | float:
    """Return x raised to the power of x."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Return a closure that repeatedly applies function to x."""
    count = 0
    value = x

    def inner() -> int | float:
        """Apply function once and return the updated value."""
        nonlocal count, value
        value = function(value)
        count += 1
        return value

    return inner
