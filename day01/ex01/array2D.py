import numpy


def slice_me(family: list, start: int, end: int) -> list:
    """
    Function that takes a 2D array, prints its shape and returns a truncated
    version based on start and end arguments using slicing method.

    Args:
        family (list): 2D array (list of lists)
        start (int): starting index for slicing
        end (int): ending index for slicing

    Returns:
        list: sliced version of the input array
    """
    if not family:
        raise ValueError("Input list cannot be empty")

    if not all(isinstance(row, list) for row in family):
        raise TypeError("All elements must be lists")

    if len(set(len(row) for row in family)) != 1:
        raise ValueError("All sublists must have the same length")

    array = numpy.array(family)
    print(f"My shape is : {array.shape}")

    result = family[start:end]

    print(f"My new shape is : ({len(result)}, {len(result[0])})")

    return result
