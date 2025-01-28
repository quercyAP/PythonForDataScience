import sys


def main():
    """Convert a string to Morse code."""
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. "
    }

    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        text = sys.argv[1]

        is_valid = all(c.upper() in NESTED_MORSE for c in text)
        assert is_valid, "the arguments are bad"

        morse = "".join(NESTED_MORSE[c.upper()] for c in text)

        print(morse.rstrip())

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
