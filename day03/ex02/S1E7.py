from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for Baratheon class"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        return f"Vector: ('{self.family_name}','{self.eyes}','{self.hairs}')"

    def __repr__(self):
        return f"Vector: ('{self.family_name}','{self.eyes}','{self.hairs}')"

    def die(self):
        """Method that changes the character's health state"""
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for Lannister class"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        return f"Vector: ('{self.family_name}','{self.eyes}','{self.hairs}')"

    def __repr__(self):
        return f"Vector: ('{self.family_name}','{self.eyes}','{self.hairs}')"

    def die(self):
        """Method that changes the character's health state"""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Class method to create a Lannister"""
        return cls(first_name, is_alive)
