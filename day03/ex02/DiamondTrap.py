from S1E7 import Baratheon, Lannister
from typing import Optional

class King(Baratheon, Lannister):
    def __init__(self, first_name: str, is_alive: Optional[bool] = True):
        """
        Constructor.

        Args:
            first_name (str): The character's name
            is_alive (Optional[bool], optional): The character's status. Defaults to True.
        """
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes: str) -> None:
        """
        Set the character's eyes color.

        Args:
            eyes (str): The eyes color

        Returns:
            None
        """
        self.eyes = eyes

    def set_hairs(self, hairs: str) -> None:
        """
        Set the character's hairs color.

        Args:
            hairs (str): The hairs color

        Returns:
            None
        """
        self.hairs = hairs

    def get_eyes(self) -> str:
        """
        Get the character's eyes color.

        Returns:
            str: The character's eyes color
        """
        return self.eyes

    def get_hairs(self) -> str:
        """
        Get the character's hairs color.

        Returns:
            str: The character's hairs color
        """
        return self.hairs
