import sys


def analyze(text: str) -> dict:
    """
    Analyze the text and count different types of characters.

    Args:
        text (str): The text to analyze

    Returns:
        dict: Dictionary containing counts of different character types
    """
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    counts = {
        'total': len(text),
        'upper': 0,
        'lower': 0,
        'punctuation': 0,
        'spaces': 0,
        'digits': 0
    }

    for char in text:
        if char.isupper():
            counts['upper'] += 1
        elif char.islower():
            counts['lower'] += 1
        elif char in punctuation:
            counts['punctuation'] += 1
        elif char.isspace():
            counts['spaces'] += 1
        elif char.isdigit():
            counts['digits'] += 1

    return counts


def display_analysis(counts: dict) -> None:
    """
    Display the analysis results in the required format.

    Args:
        counts (dict): Dictionary containing character counts
    """
    print(f"The text contains {counts['total']} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punctuation']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")


def main():
    """
    Main function that processes command line arguments and analyzes text.

    Raises:
        AssertionError: If more than one argument is provided
    """
    args = sys.argv[1:]

    try:
        if len(args) > 1:
            raise AssertionError("more than one argument is provided")

        if len(args) == 0:
            print("What is the text to count?")
            try:
                text = input()
            except EOFError:
                pass
        else:
            text = args[0]

        counts = analyze(text)
        display_analysis(counts)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
