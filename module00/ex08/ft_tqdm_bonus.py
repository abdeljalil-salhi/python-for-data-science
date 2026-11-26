"""Timed progress-bar variant kept as a bonus for module 00 ex08."""

from shutil import get_terminal_size
from time import time


def ft_tqdm(lst: range):
    """
    Print a dynamically updating progress bar with elapsed time and rate.

    This is the timed variant that was previously kept commented out in
    Loading.py. It behaves like ft_tqdm but also shows elapsed/ETA and it/s.

    Args:
        lst (range): The range to iterate through.

    Yields:
        item: The next item from the iterable.
    """
    total = len(lst)
    if total == 0:
        return

    start_time = time()
    terminal_width = get_terminal_size((80, 20)).columns - 30
    progress_bar_width = max(terminal_width - 10, 1)

    for i, item in enumerate(lst, start=1):
        progress = int(i / total * progress_bar_width)
        elapsed_time = max(time() - start_time, 1e-9)
        speed = i / elapsed_time
        eta = (total - i) / speed

        minutes, seconds = divmod(elapsed_time, 60)
        elapsed_formatted = f"{int(minutes):02d}:{int(seconds):02d}"
        minutes, seconds = divmod(eta, 60)
        eta_formatted = f"{int(minutes):02d}:{int(seconds):02d}"

        progress_bar = f"|{'█' * progress:<{progress_bar_width}}|"
        progress_percentage = progress * 100 // progress_bar_width
        progress_info = f"{progress_percentage}%{progress_bar} {i}/{total}"
        time_info = f"[{elapsed_formatted}<{eta_formatted}, {speed:.2f}it/s]"

        print(f"\r{progress_info} {time_info}", end="", flush=True)
        yield item
