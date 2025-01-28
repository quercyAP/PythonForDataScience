import sys


def ft_tqdm(lst: range) -> None:
    """
    A simplified implementation of tqdm progress bar.

    Args:
        lst (range): Range object to iterate over

    Yields:
        Elements from the input range
    """
    total = len(lst)

    for i, item in enumerate(lst, 1):
        percentage = (i / total) * 100

        bar_width = 50
        filled_length = int(bar_width * i // total)
        bar = '█' * filled_length
        empty = ' ' * (bar_width - filled_length)

        bar_str = f"\r{percentage:3.0f}%|{bar}{empty}| {i}/{total}"

        sys.stderr.write(bar_str)

        yield item
