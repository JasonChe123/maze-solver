# Use 4 bits to represent each scenario of a square with/without wall(s)
# Using IntFlag can do some bitwise operation
# Using property decorator (without declare a setter method) to make it a read-only property

from enum import IntFlag, auto


class Border(IntFlag):
    EMPTY = 0
    TOP = auto()
    BOTTOM = auto()
    LEFT = auto()
    RIGHT = auto()

    @property
    def corner(self) -> bool:
        # bitwise operation
        return self in (
            self.TOP | self.LEFT,
            self.TOP | self.RIGHT,
            self.BOTTOM | self.LEFT,
            self.BOTTOM | self.RIGHT,
        )

    @property
    def dead_end(self) -> bool:
        # if 3 bits (3 borders in a spare) which means a dead end
        return self.bit_count() == 3

    @property
    def intersection(self) -> bool:
        # if only 1 bit (1 border in a spare) which means a T (intersection)
        return self.bit_count() < 2
