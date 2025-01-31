import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random 15-character lowercase string"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


def generate_login(name: str, surname: str) -> str:
    """Generate login from name and surname"""
    return (name.capitalize() + surname.capitalize()) + " "


@dataclass
class Student:
    """A student class with auto-generated id and login"""
    name: str = field(default="")
    surname: str = field(default="")
    active: bool = field(default=True, init=False)
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """Post initialization to set login and add spaces to name/surname"""
        self.name = self.name + " "
        self.surname = self.surname + " "
        self.login = generate_login(self.name, self.surname)
