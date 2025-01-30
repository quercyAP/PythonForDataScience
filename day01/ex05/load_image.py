import numpy
from PIL import Image


def ft_load(path: str) -> numpy.ndarray:
    """
    Load an image file and return its pixel data as a numpy array.

    Args:
        path (str): Path to the image file

    Returns:
        np.ndarray: Array of pixel values in RGB format

    Raises:
        FileNotFoundError: If the image file doesn't exist
        ValueError: If the file is not a valid image
    """
    try:
        with Image.open(path) as img:
            if img.mode != 'RGB':
                img = img.convert('RGB')

            array = numpy.array(img)

            print(f"The shape of image is: {array.shape}")

            return array

    except FileNotFoundError:
        raise FileNotFoundError(f"Error: No such file: '{path}'")
    except Exception as e:
        raise ValueError(f"Error: Unable to load image: {str(e)}")
