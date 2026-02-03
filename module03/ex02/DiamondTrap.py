from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Class representing a King character.
    """

    def __init__(self, first_name, is_alive: bool = True) -> None:
        """
        Initializes a King instance, inheriting from Baratheon and Lannister.

        Args:
            first_name (str): The first name of the King character.
            is_alive (bool): Boolean indicating if the character is alive.
        """
        super().__init__(first_name, is_alive)

    def set_eyes(self, color: str) -> None:
        """
        Sets the eye color of the King character.

        Args:
            color (str): The new eye color.
        """
        self.eyes = color

    def set_hairs(self, color: str) -> None:
        """
        Sets the hair color of the King character.

        Args:
            color (str): The new hair color.
        """
        self.hairs = color

    def get_eyes(self) -> str:
        """
        Gets the eye color of the King character.

        Returns:
            str: The eye color.
        """
        return self.eyes

    def get_hairs(self) -> str:
        """
        Gets the hair color of the King character.

        Returns:
            str: The hair color.
        """
        return self.hairs
