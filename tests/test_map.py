from unittest import TestCase
from levelup.map import GameMap
from levelup.position import Position

class TestMap(TestCase):
    def test_initialization(self):
        test_map = GameMap()
        expected_map_size: Tuple[int, int] = (9, 9)
        expected_map_starting_position: Position = Position(0, 0)
        expected_map_position_count = 0

        self.assertEqual(expected_map_starting_position, test_map.starting_position)
        self.assertEqual(expected_map_size, test_map.size)
        self.assertEqual(expected_map_position_count, test_map.position_count)



    def test_valid_position(self):
        test_map = GameMap()
        test_position_values = []
        for i in range(10):
            for j in range(10):
               booleanValue = test_map.is_valid_position(Position(i, j))
               self.assertEqual(booleanValue,True)
    

       