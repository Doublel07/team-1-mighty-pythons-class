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
        self.positions = []
        for x in [i for i in range(0, self.size[0])]:
            for y in [i for i in range(0, self.size[1])]:
                self.positions.append(Position(x, y))
        
        #self.position_count = (x + 1) * (y + 1)

    def is_valid_position(self, position: Position) -> bool:
       #return position in self.positions 
        # Check Position X, Y Coordinate is Valid
        if position.coordinates[0] <= 9 and position.coordinates[0] >= 0 and position.coordinates[1] <= 9 and position.coordinates[1] >= 0:
            return True
        else:
            return False
        

    def calculate_position(
        self, starting_position: Position, direction: Direction
    ) -> Position:
        # determine if the position calculated is valid
        x, y = starting_position.coordinates
        if direction is Direction.NORTH:
            y += 1
        elif direction is Direction.SOUTH:
            y -= 1
        elif direction is Direction.EAST:
            x += 1
        elif direction is Direction.WEST:
            x -= 1

        return Position(x, y)
        
    