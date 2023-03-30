from enum import Enum
from typing import Tuple, List
from levelup.position import Position


class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"


class GameMap:
    starting_position: Position = Position(0, 0)
    size: Tuple[int, int] = (9, 9)
    position_count: int = 0
    positions: List[Position]

    def __init__(self):
        self.create_positions()

    def create_positions(self) -> None:
        pass

    def is_valid_position(self, position: Position) -> bool:
        
        # Check Position X, Y Coordinate is Valid
        if position.coordinates[0] <= 9 and position.coordinates[0] >= 0 and position.coordinates[1] <= 9 and position.coordinates[1] >= 0:
            return True
        else:
            return False
        

    def calculate_position(
        self, starting_position: Position, direction: Direction
    ) -> Position:
        # determine if the position calculated is valid
        pass
