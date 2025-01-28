def ft_filter(function, iterable):
    """Filter items from the iterable based on a function.

    Args:
        function: callable or None - filtering function to apply
        iterable: input sequence to filter

    Returns:
        List containing items for which function(item) is true,
        or items that are true if function is None.
    """
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]
