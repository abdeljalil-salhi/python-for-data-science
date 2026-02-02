import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image from the given path (supports at least JPG/JPEG),
    prints its format and RGB pixel content shape,
    and returns the image as a NumPy array in shape (height, width, 3).

    Raises clear error messages for unsupported formats or invalid files.
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
