def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """Calculate the body mass index (BMI) from height and weight.

    Args:
        height (list[int | float]): List of heights in meters
        weight (list[int | float]): List of weights in kg

    Returns:
        list[int | float]: List of BMIs

    Raises:
        ValueError: If inputs are not the same size or contain invalid values
    """
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same length")
    if not all(isinstance(h, (int, float)) for h in height) or \
       not all(isinstance(w, (int, float)) for w in weight):
        raise ValueError("All elements must be int or float")
    if not all(h > 0 for h in height) or not all(w > 0 for w in weight):
        raise ValueError("All values must be positive")

    return [w / (h * h) for w, h in zip(weight, height)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Apply a limit to a list of BMIs.

    Args:
        bmi (list[int | float]): List of BMIs
        limit (int): Limit to apply

    Returns:
        list[bool]: List of booleans (True if above or equal to limit)

    Raises:
        ValueError: If input is not a valid list of numbers
    """
    if not all(isinstance(b, (int, float)) for b in bmi):
        raise ValueError("All BMI values must be int or float")

    return [b >= limit for b in bmi]
