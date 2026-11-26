from typing import Any


def _mean(values: list[Any]) -> float:
    """Return the arithmetic mean of the given values."""
    return sum(values) / len(values)


def _median(values: list[Any]) -> int | float:
    """Return the median of the given values."""
    ordered = sorted(values)
    size = len(ordered)
    middle = size // 2
    if size % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def _percentile(values: list[Any], quantile: float) -> float:
    """Return a linearly interpolated percentile of the given values."""
    ordered = sorted(values)
    position = (len(ordered) - 1) * quantile
    lower = int(position)
    upper = min(lower + 1, len(ordered) - 1)
    return ordered[lower] + (ordered[upper] - ordered[lower]) * (
        position - lower
    )


def _quartile(values: list[Any]) -> list[float]:
    """Return the 25th and 75th percentiles of the given values."""
    return [_percentile(values, 0.25), _percentile(values, 0.75)]


def _variance(values: list[Any]) -> float:
    """Return the population variance of the given values."""
    mean = _mean(values)
    return sum((value - mean) ** 2 for value in values) / len(values)


def _std(values: list[Any]) -> float:
    """Return the population standard deviation of the given values."""
    return _variance(values) ** 0.5


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Print each requested statistic computed from args."""
    handlers = {
        "mean": _mean,
        "median": _median,
        "quartile": _quartile,
        "std": _std,
        "var": _variance,
    }
    values = list(args)

    for statistic in kwargs.values():
        if not isinstance(statistic, str) or statistic not in handlers:
            continue
        try:
            print(f"{statistic} : {handlers[statistic](values)}")
        except Exception:
            print("ERROR")
