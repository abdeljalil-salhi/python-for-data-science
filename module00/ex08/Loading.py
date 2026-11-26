from shutil import get_terminal_size


def ft_tqdm(lst: range):
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.

    Args:
        lst (range): The range to iterate through.

    Yields:
        item: The next item from the iterable.
    """
    total = len(lst)
    if total == 0:
        return

    bar_width = max(get_terminal_size((80, 20)).columns - 40, 1)

    for i, item in enumerate(lst, 1):
        frac = i / total
        filled = int(bar_width * frac)
        if filled >= bar_width:
            bar = "=" * (bar_width - 1) + ">"
        else:
            bar = "=" * max(filled - 1, 0) + ">"
            bar += " " * (bar_width - filled)

        percent = int(frac * 100)
        print(f"\r{percent:3d}%|{bar}| {i}/{total}", end="", flush=True)
        yield item
