class calculator:
    """
    Calculator class able to perform vector operations.
    (addition, multiplication, substraction, division)
    """

    def __init__(self, vector: list) -> None:
        self.vector = vector

    def __add__(self, scalar: int) -> None:
        """Add two vectors"""
        self.vector = [x + scalar for x in self.vector]
        print(self.vector)

    def __mul__(self, scalar: int) -> None:
        """Multiply two vectors"""
        self.vector = [x * scalar for x in self.vector]
        print(self.vector)

    def __sub__(self, scalar: int) -> None:
        """Substract two vectors"""
        self.vector = [x - scalar for x in self.vector]
        print(self.vector)

    def __truediv__(self, scalar: int) -> None:
        """Divide two vectors"""
        if scalar == 0:
            raise ZeroDivisionError("scalar cannot be zero")
        self.vector = [x / scalar for x in self.vector]
        print(self.vector)
