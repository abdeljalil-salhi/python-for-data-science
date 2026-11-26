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

    @property
    def eyes(self) -> str:
        """Return the eye colour stored on this instance."""
        return self.__dict__["eyes"]

    @eyes.setter
    def eyes(self, color: str) -> None:
        """Store the eye colour on this instance."""
        self.__dict__["eyes"] = color

    @property
    def hairs(self) -> str:
        """Return the hair colour stored on this instance."""
        return self.__dict__.get("hairs", self.__dict__.get("hair", ""))

    @hairs.setter
    def hairs(self, color: str) -> None:
        """Store the hair colour on this instance."""
        self.__dict__.pop("hairs", None)
        self.__dict__["hair"] = color

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
        self.__dict__.pop("hair", None)
        self.__dict__["hairs"] = color

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
        return self.__dict__.get("hairs", self.__dict__.get("hair", ""))
