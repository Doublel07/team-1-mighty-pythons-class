from unittest import TestCase
from levelup.map import GameMap
from levelup.position import Position

class TestMap(TestCase):
    def test_init(self):
        test_map = GameMap()
        expected_map_size: Tuple[int, int] = (9, 9)
        expected_map_starting_position: Position = Position(0, 0)

        self.assertEqual(expected_map_starting_position, test_map.starting_position)
        self.assertEqual(expected_map_size, test_map.size)
        self.assertIsNone(test_map.position_count)
        self.assertIsNone(test_map.positions)



