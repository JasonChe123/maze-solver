from dataclasses import dataclass
from maze_solver.models.border import Border
from maze_solver.models.role import Role


# set frozen=True to avoid changing after declared it
@dataclass(frozen=True)
class Square:
    index: int
    row: int
    column: int
    border = Border
    role: Role = Role.NONE
