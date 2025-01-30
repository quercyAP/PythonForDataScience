from S1E9 import Character
from typing import Optional

class Baratheon(Character):
    """
    Class representing the Baratheon family.
    """
    def __init__(self, first_name: str, is_alive: Optional[bool] = True):
        """
        Constructor.

        Args:
            first_name (str): The character's name
            is_alive (Optional[bool], optional): The character's status. Defaults to True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self) -> str:
        """
        Return a string representation of the character.
        
        Returns:
            str: The character's name
        """
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self) -> str:
        """
        Return a string representation of the character.
        
        Returns:
            str: The character's name
        """
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"
    
    def die(self) -> None:
        """
        Kill the character.

        Returns:
            None
        """
        self.is_alive = False

class Lannister(Character):
    """
    Class representing the Lannister family.
    """
    def __init__(self, first_name: str, is_alive: Optional[bool] = True):
        """
        Constructor.

        Args:
            first_name (str): The character's name
            is_alive (Optional[bool], optional): The character's status. Defaults to True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self) -> str:
        """
        Return a string representation of the character.
        
        Returns:
            str: The character's name
        """
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"
    
    def __repr__(self) -> str:
        """ 
        Return a string representation of the character.
        
        Returns:
            str: The character's name
        """
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"
    
    def die(self) -> None:
        """
        Kill the character.

        Returns:
            None
        """
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: Optional[bool] = True):
        """
        Create a new Lannister character.

        Args:
            first_name (str): The character's name
            is_alive (Optional[bool], optional): The character's status. Defaults to True.
        
        Returns:
            Lannister: The new character
        """
        return cls(first_name, is_alive)