from unittest import TestCase
from levelup.map import GameMap


class TestMap(TestCase):
    def test_init(self):
        test_map = GameMap()
        expected_map_minimum_value: Tuple[int, int] = (0, 0)
        expected_map_maximum_value: Tuple[int, int] = (9, 9)

        self.assertEqual(expected_map_minimum_value, test_map.minimum_value)
        self.assertEqual(expected_map_maximum_value, test_map.maximum_value)
        self.assertIsNone(test_map.value)




