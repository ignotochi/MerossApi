from dataclasses import dataclass

@dataclass
class Auth:
    user: str = ""
    password: str = ""