from callLimit import callLimit


@callLimit(3)
def f():
    """Print the f marker."""
    print("f()")


@callLimit(1)
def g():
    """Print the g marker."""
    print("g()")


def main() -> None:
    """Run the decorator example from the subject."""
    for i in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
