import sys


def is_integer(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False


args = sys.argv[1:]

try:
    if len(args) > 0:
        if len(args) > 1:
            raise AssertionError("more than one argument is provided")

        if not is_integer(args[0]):
            raise AssertionError("argument is not an integer")

        number = int(args[0])
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
except AssertionError as e:
    print(f"AssertionError: {str(e)}")
