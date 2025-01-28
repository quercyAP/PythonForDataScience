import sys
from ft_filter import ft_filter


def is_valid_string(s: str) -> bool:
    """Check if string contains only letters, numbers and spaces."""
    return all(c.isalnum() or c.isspace() for c in s)


def main():
    """
    Filter words from a string based on their length.
    Usage: python filterstring.py <string> <length>
    """
    try:
        assert len(sys.argv) == 3, "the arguments are bad"

        text, length = sys.argv[1], sys.argv[2]
        assert isinstance(text, str), "the arguments are bad"
        assert is_valid_string(text), "the arguments are bad"
        assert length.isdigit(), "the arguments are bad"
        length = int(length)

        words = text.split()
        filtered_words = list(ft_filter(lambda x: len(x) > length, words))

        print(filtered_words)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
