def square(x: int | float) -> int | float:
    """Return the square of x"""
    return x * x


def pow(x: int | float) -> int | float:
    """Return x raised to the power of x"""
    return x ** x


def outer(x: int | float, function) -> object:
    """Return an inner function that applies the given function repeatedly"""
    count = 0
    result = x

    def inner() -> float:
        """Apply the function to the result, updating it each time"""
        nonlocal count, result
        if count == 0:
            result = function(result)
        else:
            result = function(result)
        count += 1
        return result

    return inner
