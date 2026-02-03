import sys


class calculator:
    """
    A simple calculator class that performs arithmetic operations on a
    list of floating-point numbers.
    """

    def __init__(self, vector: list[float]) -> None:
        """
        Initializes the calculator with a list of floats.

        Args:
            vector (list[float]): A list of floating-point numbers.
        """
        self.vector: list[float] = vector

    def __add__(self, object: float) -> None:
        """
        Adds the object to each element in the vector.

        Args:
            object (float): The number to add to each element.
        """
        self.vector = [num + object for num in self.vector]
        print(self.vector)

    def __mul__(self, object: float) -> None:
        """
        Multiplies each element in the vector by the object.

        Args:
            object (float): The number to multiply each element by.
        """
        self.vector = [num * object for num in self.vector]
        print(self.vector)

    def __sub__(self, object: float) -> None:
        """
        Subtracts the object from each element in the vector.

        Args:
            object (float): The number to subtract from each element.
        """
        self.vector = [num - object for num in self.vector]
        print(self.vector)

    def __truediv__(self, object: float) -> None:
        """
        Divides each element in the vector by the object.

        Args:
            object (float): The number to divide each element by.

        Raises:
            ZeroDivisionError: If the object is zero.
        """
        try:
            if object == 0:
                raise ZeroDivisionError("division by zero is not allowed")
            self.vector = [num / object for num in self.vector]
            print(self.vector)
        except ZeroDivisionError as e:
            print(
                f"{ZeroDivisionError.__name__}: {e}",
                file=sys.stderr,
            )

    def __str__(self) -> str:
        """
        Returns a string representation of the vector.
        """
        return str(self.vector)

    def __repr__(self) -> str:
        """
        Returns a string representation of the vector.
        """
        return self.__str__()
