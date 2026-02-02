from os import get_terminal_size


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

    width = get_terminal_size().columns - 30
    bar_width = width - 10

    for i, item in enumerate(lst, 1):
        frac = i / total
        filled = int(bar_width * frac)

        bar = "█" * filled + " " * (bar_width - filled)
        percent = int(frac * 100)

        line = f"{percent:3d}%|{bar}| {i}/{total}"

        print("\r" + line, end="", flush=True)
        yield item


"""
def ft_tqdm(lst: range):
    from time import time

    total = len(lst)
    start_time = time()

    terminal_width = get_terminal_size().columns - 30
    progress_bar_width = terminal_width - 10

    for i, item in enumerate(lst, start=1):
        progress = int(i / total * progress_bar_width)
        elapsed_time = time() - start_time
        speed = i / elapsed_time
        eta = (total - i) / speed

        m, s = divmod(elapsed_time, 60)
        elapsed_formatted = f"{int(m):02d}:{int(s):02d}"
        m, s = divmod(eta, 60)
        eta_formatted = f"{int(m):02d}:{int(s):02d}"

        progress_bar = f"|{'█' * progress:<{progress_bar_width}}|"
        progress_percentage = progress * 100 // progress_bar_width
        progress_info = f"{progress_percentage}%{progress_bar} {i}/{total}"
        time_info = f"[{elapsed_formatted}<{eta_formatted}, {speed:.2f}it/s]"

        print(f"\r{progress_info} {time_info}", end="", flush=True)
        yield item
"""
