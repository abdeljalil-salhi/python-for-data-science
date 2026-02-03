from S1E9 import Character


class Baratheon(Character):
    """
    Class representing a Baratheon character.
    """

    def __init__(
        self,
        first_name: str,
        is_alive: bool = True,
    ) -> None:
        """
        Initializes a Baratheon instance, inheriting from Character.

        Args:
            first_name (str): The first name of the Baratheon character.
            is_alive (bool): Boolean indicating if the character is alive.
        """
        super().__init__(first_name, is_alive)
        self.family_name: str = "Baratheon"
        self.eyes: str = "brown"
        self.hairs: str = "dark"

    def die(self) -> None:
        """
        Marks the Baratheon character as dead.
        """
        self.is_alive = False

    def __str__(self) -> str:
        """
        Returns a string representation of the Baratheon character.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """
        Returns a string representation of the Baratheon character.
        """
        return self.__str__()


class Lannister(Character):
    """
    Class representing a Lannister character.
    """

    def __init__(
        self,
        first_name: str,
        is_alive: bool = True,
    ) -> None:
        """
        Initializes a Lannister instance, inheriting from Character.

        Args:
            first_name (str): The first name of the Lannister character.
            is_alive (bool): Boolean indicating if the character is alive.
        """
        super().__init__(first_name, is_alive)
        self.family_name: str = "Lannister"
        self.eyes: str = "blue"
        self.hairs: str = "light"

    def die(self) -> None:
        """
        Marks the Lannister character as dead.
        """
        self.is_alive = False

    @classmethod
    def create_lannister(
        cls,
        first_name: str,
        is_alive: bool = True,
    ) -> "Lannister":
        """
        Class method to create a Lannister instance.

        Args:
            first_name (str): The first name of the Lannister character.
            is_alive (bool): Boolean indicating if the character is alive.

        Returns:
            Lannister: A new instance of Lannister.
        """
        return cls(first_name, is_alive)

    def __str__(self) -> str:
        """
        Returns a string representation of the Lannister character.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """
        Returns a string representation of the Lannister character.
        """
        return self.__str__()
