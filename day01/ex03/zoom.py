from load_image import ft_load
import matplotlib.pyplot


def main():
    try:
        img = ft_load("animal.jpeg")
        print(img)

        center_y = 299
        center_x = 665

        zoom_size = 200

        start_y = center_y - zoom_size
        end_y = center_y + zoom_size
        start_x = center_x - zoom_size
        end_x = center_x + zoom_size

        zoomed = img[start_y:end_y, start_x:end_x, 0:1]

        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)

        matplotlib.pyplot.figure(figsize=(6, 6))

        matplotlib.pyplot.subplot(1, 1, 1)
        matplotlib.pyplot.imshow(zoomed, cmap="gray")

        matplotlib.pyplot.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
