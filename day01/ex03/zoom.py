from load_image import ft_load
import matplotlib.pyplot


def main():
    try:
        # Load the image
        img = ft_load("day01/assets/animal.jpeg")
        print(img)

        # Calculate the center point for zooming
        height, width = img.shape[:2]
        center_y = height // 2
        center_x = width // 2

        # Define the zoom window size (400x400)
        zoom_size = 200

        # Calculate the boundaries for the zoom window
        start_y = center_y - zoom_size
        end_y = center_y + zoom_size
        start_x = center_x - zoom_size
        end_x = center_x + zoom_size

        # Extract the zoomed portion (taking only one channel)
        zoomed = img[start_y:end_y, start_x:end_x, 0:1]

        # Print the new shape
        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)

        # Display the original and zoomed images
        matplotlib.pyplot.figure(figsize=(12, 6))

        matplotlib.pyplot.subplot(1, 2, 1)
        matplotlib.pyplot.imshow(img)
        matplotlib.pyplot.title("Original Image")

        matplotlib.pyplot.subplot(1, 2, 2)
        matplotlib.pyplot.imshow(zoomed.squeeze(), cmap='gray')
        matplotlib.pyplot.title("Zoomed Region (Single Channel)")

        matplotlib.pyplot.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
