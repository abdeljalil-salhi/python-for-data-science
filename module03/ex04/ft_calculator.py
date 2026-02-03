class calculator:
    """
    A simple calculator class that performs arithmetic operations on a
    list of floating-point numbers.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        @staticmethod

        Calculates the dot product of two vectors and prints the result.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.
        """
        dot_product = 0

        i = 0
        while i < len(V1):
            dot_product += V1[i] * V2[i]
            i += 1

        print(f"Dot Product is: {int(dot_product)}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        @staticmethod

        Adds two vectors element-wise and prints the result vector.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.
        """
        tmp = []

        i = 0
        while i < len(V1):
            tmp.append(float(V1[i] + V2[i]))
            i += 1

        print(f"Add Vector is : {tmp}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        @staticmethod

        Subtracts the second vector from the first vector element-wise and
        prints the result vector.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.
        """
        tmp = []

        i = 0
        while i < len(V1):
            tmp.append(float(V1[i] - V2[i]))
            i += 1

        print(f"Sous Vector is: {tmp}")
