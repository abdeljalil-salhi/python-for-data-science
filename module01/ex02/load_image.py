import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image from the given path (supports JPG/JPEG),
    prints its RGB pixel content shape,
    and returns the image as a NumPy array in shape (height, width, 3).

    Args:
        path (str): The file path to the image.

    Returns:
        np.ndarray: The image as a NumPy array with shape (height, width, 3).

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file format is unsupported or cannot be identified.
        RuntimeError: For other errors during image loading.
    """
    try:
        img = Image.open(path)

        if img.mode != "RGB":
            img = img.convert("RGB")

        # shape is (height, width, 3)
        array = np.array(img)

        h, w, c = array.shape
        print(f"The shape of image is: ({h}, {w}, {c})")

        return array

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")

    except Image.UnidentifiedImageError:
        raise ValueError(
            f"Cannot identify image file format: {path} "
            "(supported: JPEG/JPG at minimum)"
        )

    except Exception as e:
        raise RuntimeError(f"Error loading image '{path}': {str(e)}")
