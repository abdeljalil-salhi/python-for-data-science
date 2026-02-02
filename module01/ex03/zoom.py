import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from load_image import ft_load


def main(path: str = "animal.jpeg") -> None:
    """
    Main function to load an image, zoom into it, and display the result.

    Args:
        path (str): Path to the image file. Defaults to "animal.jpeg".
    """
    try:
        array, h, w = ft_load(path)
        print(array)

        target_size = 400
        if h < target_size or w < target_size:
            raise ValueError(
                f"Image is too small ({h}x{w}). "
                f"Need at least {target_size}x{target_size}"
            )

        # Center crop
        start_y = (h - target_size) // 2
        start_x = (w - target_size) // 2
        zoomed = array[
            start_y: start_y + target_size,
            start_x: start_x + target_size
        ]

        gray = np.mean(zoomed, axis=-1, keepdims=True).astype(np.uint8)

        print(f"New shape after slicing: {gray.shape}")
        print(gray)

        plt.figure(figsize=(7, 7))
        plt.imshow(gray.squeeze(), cmap='gray')
        plt.axis('on')

        plt.show()
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.", file=sys.stderr)
        sys.exit(1)
    except Image.UnidentifiedImageError:
        print(f"Error: Cannot open '{path}' — \
            unsupported or corrupted image format.", file=sys.stderr)
        sys.exit(1)
    except ValueError as ve:
        print(f"Value error: {ve}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error while processing '{path}': \
            {type(e).__name__} - {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
