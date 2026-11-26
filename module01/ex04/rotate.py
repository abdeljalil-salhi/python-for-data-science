import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from load_image import ft_load


def manual_transpose(arr: np.ndarray) -> np.ndarray:
    """
    Manually transpose a 2D array.

    Args:
        arr (np.ndarray): Input 2D array to transpose.

    Returns:
        np.ndarray: Transposed 2D array.
    """
    if arr.ndim != 2:
        raise ValueError("manual_transpose expects a 2D array")

    old_height, old_width = arr.shape
    transposed = np.zeros((old_width, old_height), dtype=arr.dtype)

    for y in range(old_height):
        for x in range(old_width):
            transposed[x, y] = arr[y, x]

    return transposed


def main(path: str = "animal.jpeg") -> None:
    """
    Main function to load an image, transpose it, and display the result.

    Args:
        path (str): Path to the image file. Defaults to "animal.jpeg".
    """
    try:
        array, h, w = ft_load(path, verbose=False)

        target_size = 400
        if h < target_size or w < target_size:
            raise ValueError(
                f"Image is too small ({h}x{w}). "
                f"Need at least {target_size}x{target_size}"
            )

        # Center crop
        start_y = (h - target_size) // 2
        start_x = (w - target_size) // 2
        cropped = array[
            start_y: start_y + target_size,
            start_x: start_x + target_size
        ]

        gray = np.mean(cropped, axis=-1).astype(np.uint8)

        print(f"The shape of image is: {gray.shape}")
        print(gray)

        transposed = manual_transpose(gray)

        print("New shape after Transpose:", transposed.shape)
        print(transposed)

        plt.figure(figsize=(7, 7))
        plt.imshow(transposed.squeeze(), cmap='gray')
        plt.axis('on')

        plt.show()

    except FileNotFoundError:
        print(f"Error: File '{path}' not found.", file=sys.stderr)
        sys.exit(1)
    except Image.UnidentifiedImageError:
        print(
            f"Error: Cannot open '{path}' — "
            "unsupported or corrupted image format.",
            file=sys.stderr,
        )
        sys.exit(1)
    except ValueError as ve:
        print(f"Value error: {ve}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(
            f"Unexpected error while processing '{path}': "
            f"{type(e).__name__} - {e}",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
