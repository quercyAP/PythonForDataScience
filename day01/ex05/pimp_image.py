import numpy


def ft_invert(array: numpy.ndarray) -> numpy.ndarray:
    """
    Inverts the color of the image reveived.

    Args:
        array (numpy.ndarray): 2D array representing the image

    Returns:
        numpy.ndarray: Inverted image
    """
    return 255 - array


def ft_red(array: numpy.ndarray) -> numpy.ndarray:
    """
    Keeps only the red channel in the image.

    Args:
        array (numpy.ndarray): 2D array representing the image

    Returns:
        numpy.ndarray: Image with only the red channel
    """
    result = array.copy()
    result[:, :, 1] = 0
    result[:, :, 2] = 0
    return result


def ft_green(array: numpy.ndarray) -> numpy.ndarray:
    """
    Keeps only the green channel in the image.

    Args:
        array (numpy.ndarray): 2D array representing the image

    Returns:
        numpy.ndarray: Image with only the green channel
    """
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 2] = 0
    return result


def ft_blue(array: numpy.ndarray) -> numpy.ndarray:
    """
    Keeps only the blue channel in the image.

    Args:
        array (numpy.ndarray): 2D array representing the image

    Returns:
        numpy.ndarray: Image with only the blue channel
    """
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 1] = 0
    return result


def ft_add(a, b):
    """
    Implements addition using only bitwise operations.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b using bitwise operations
    """
    while numpy.any(b != 0):
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a


def ft_grey(array: numpy.ndarray) -> numpy.ndarray:
    """
    Converts the image to grayscale using simple averaging method.
    Formula: (Red + Green + Blue) / 3

    Args:
        array (numpy.ndarray): 3D array representing the RGB image

    Returns:
        numpy.ndarray: Grayscale image
    """
    result = array.copy()
    grey = (
        ft_add(
            ft_add(result[:, :, 0].astype(int), result[:, :, 1].astype(int)),
            result[:, :, 2].astype(int),
        )
        / 3
    )

    result[:, :, 0] = grey
    result[:, :, 1] = grey
    result[:, :, 2] = grey
    return result
