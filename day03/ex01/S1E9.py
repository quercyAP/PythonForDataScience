from abc import ABC, abstractmethod


class Character(ABC):
    """A class representing Game of Thrones characters"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for Character class"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Method that changes the character's health state"""
        pass


class Stark(Character):
    """A class representing the Stark family"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for Stark class"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Method that changes the character's health state"""
        self.is_alive = False
