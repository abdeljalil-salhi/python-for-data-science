import numpy as np
from PIL import Image


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the color of the image received.
    """
    inverted = 255 - array
    Image.fromarray(inverted.astype(np.uint8)).show()
    return inverted.astype(np.uint8)


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Applies a red filter to the image (keeps only red channel).
    """
    red = array.copy()
    # Set green and blue to 0
    red[..., 1] = 0 * red[..., 1]
    red[..., 2] = 0 * red[..., 2]
    Image.fromarray(red.astype(np.uint8)).show()
    return red.astype(np.uint8)


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Applies a green filter to the image (keeps only green channel).
    """
    green = array.copy()
    # Set red and blue to 0
    green[..., 0] = green[..., 0] - green[..., 0]
    green[..., 2] = green[..., 2] - green[..., 2]
    Image.fromarray(green.astype(np.uint8)).show()
    return green.astype(np.uint8)


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Applies a blue filter to the image (keeps only blue channel).
    """
    blue = array.copy()
    # Set red and green to 0 using only assignment
    blue[..., 0] = 0
    blue[..., 1] = 0
    Image.fromarray(blue.astype(np.uint8)).show()
    return blue.astype(np.uint8)


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Applies a grey filter to the image (simple average of channels).
    """
    # Average of the three channels.
    grey = array.sum(axis=-1) / 3
    # Make it 3-channel grey (same value in R,G,B)
    grey_3ch = np.stack([grey, grey, grey], axis=-1)
    Image.fromarray(grey_3ch.astype(np.uint8)).show()
    return grey_3ch.astype(np.uint8)
