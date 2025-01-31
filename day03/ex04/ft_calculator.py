class calculator:
    """
    Calculator class able to perform vector operations.
    (addition, substraction, dot product) of two vectors.
    """

    @staticmethod
    def dotproduct(V1: list[float], v2: list[float]) -> None:
        """Return the dot product of two vectors"""
        print("Dot product is: ", sum(V1[i] * v2[i] for i in range(len(V1))))

    @staticmethod
    def add_vec(V1: list[float], v2: list[float]) -> None:
        """Return the sum of two vectors"""
        print("Add Vector is: ", [V1[i] + v2[i] for i in range(len(V1))])

    @staticmethod
    def sous_vec(V1: list[float], v2: list[float]) -> None:
        """Return the substraction of two vectors"""
        print("Sous Vector is: ", [V1[i] - v2[i] for i in range(len(V1))])