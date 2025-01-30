from abc import ABC, abstractmethod
from typing import Optional


class Character(ABC):
    """
    Abstract class representing a character.
    """

    @abstractmethod
    def __init__(self, first_name: str, is_alive: Optional[bool] = True):
        """
        Constructor.

        Args:
            first_name (str): The character's name
            is_alive (Optional[bool], optional): The character's status. Defaults to True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> None:
        pass


class Stark(Character):
    """
    Class representing the Stark family.
    """

    def __init__(self, first_name: str, is_alive: Optional[bool] = True):
        """
        Constructor.

        Args:
            first_name (str): The character's name
            is_alive (Optional[bool], optional): The character's status. Defaults to True.
        """
        super().__init__(first_name, is_alive)

    def die(self) -> None:
        """
        Kill the character.

        Returns:
            None
        """
        self.is_alive = False
