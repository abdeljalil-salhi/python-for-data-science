from functools import wraps
from typing import Any


def callLimit(limit: int):
    """Return a decorator that blocks calls beyond limit."""
    count = 0

    def callLimiter(function):
        """Wrap function with the call-limit check."""

        @wraps(function)
        def limit_function(*args: Any, **kwds: Any):
            """Call function until the limit is reached, then report."""
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                return None
            count += 1
            return function(*args, **kwds)

        return limit_function

    return callLimiter
