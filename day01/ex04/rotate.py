from load_image import ft_load
import matplotlib.pyplot
import numpy


def transpose(array: numpy.ndarray) -> numpy.ndarray:
    """
    Transpose a 2D array.

    Args:
        array (numpy.ndarray): 2D array

    Returns:
        numpy.ndarray: Transposed array
    """
    array = array.squeeze()
    height, width = array.shape[:2]
    transposed = numpy.zeros((width, height), dtype=array.dtype)

    for i in range(height):
        for j in range(width):
            transposed[j, i] = array[i, j]

    return transposed


def main():
    try:
        img = ft_load("day01/assets/animal.jpeg")

        center_y = 299
        center_x = 665

        zoom_size = 200

        start_y = center_y - zoom_size
        end_y = center_y + zoom_size
        start_x = center_x - zoom_size
        end_x = center_x + zoom_size

        zoomed = img[start_y:end_y, start_x:end_x, 0:1]

        print(f"The shape of image is: {zoomed.shape}")
        print(zoomed)

        transposed = transpose(zoomed)

        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)

        matplotlib.pyplot.figure(figsize=(6, 6))

        matplotlib.pyplot.subplot(1, 1, 1)
        matplotlib.pyplot.imshow(transposed, cmap='gray')

        matplotlib.pyplot.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
