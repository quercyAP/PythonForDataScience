from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib.pyplot


def display(img, title):
    matplotlib.pyplot.figure(figsize=(6, 6))
    matplotlib.pyplot.imshow(img)
    matplotlib.pyplot.title(title)
    matplotlib.pyplot.show()


img = ft_load("landscape.jpg")

filters = [
    (ft_invert, "Invert"),
    (ft_red, "Red"),
    (ft_green, "Green"),
    (ft_blue, "Blue"),
    (ft_grey, "Grey"),
]

for func, title in filters:
    new_img = func(img)
    display(new_img, title)
    if title == "Invert":
        print(func.__doc__)
