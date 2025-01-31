from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, first_name):
        """Constructor for King class"""
        super().__init__(first_name)

    def get_eyes(self):
        """Get the character's eyes color"""
        return self.eyes

    def get_hairs(self):
        """Get the character's hairs color"""
        return self.hairs

    def set_eyes(self, eyes):
        """Set the character's eyes color"""
        self.eyes = eyes + " "

    def set_hairs(self, hairs):
        """Set the character's hairs color"""
        self.hairs = hairs + " "
