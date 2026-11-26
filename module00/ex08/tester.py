import sys
from time import sleep

from tqdm import tqdm

from ft_tqdm_bonus import ft_tqdm as ft_tqdm_bonus
from Loading import ft_tqdm


def main() -> None:
    """Compare the custom, original and timed progress bars in one run."""
    print("--- ft_tqdm ---", flush=True)
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()

    print("--- tqdm ---", flush=True)
    for elem in tqdm(range(333), file=sys.stdout):
        sleep(0.005)
    print()

    print("--- ft_tqdm_bonus ---", flush=True)
    for elem in ft_tqdm_bonus(range(333)):
        sleep(0.005)
    print()


if __name__ == "__main__":
    main()
