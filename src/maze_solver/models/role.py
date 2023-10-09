from enum import IntEnum, auto


class Role(IntEnum):
    """Used to define each square. Use Enum to avoid reassigning values."""
    NONE = 0
    ENEMY = auto()
    ENTRANCE = auto()
    EXIT = auto()
    EXTERIOR = auto()
    REWARD = auto()
    WALL = auto()
