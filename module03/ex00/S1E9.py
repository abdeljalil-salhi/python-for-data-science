from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract base class representing a character.
    """

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Initializes a Character instance.

        :param first_name: The first name of the character.
        :param is_alive: Boolean indicating if the character is alive.
        """
        self.first_name: str = first_name
        self.is_alive: bool = is_alive

    @abstractmethod
    def die(self) -> None:
        """
        Abstract method to handle character death.

        Should be implemented by subclasses.
        """
        pass


class Stark(Character):
    """
    Class representing a Stark character.
    """

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Initializes a Stark instance, inheriting from Character.

        :param first_name: The first name of the Stark character.
        :param is_alive: Boolean indicating if the character is alive.
        """
        super().__init__(first_name, is_alive)

    def die(self) -> None:
        """
        Marks the Stark character as dead.
        """
        self.is_alive = False
