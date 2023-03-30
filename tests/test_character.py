from unittest import TestCase
from levelup.character import Character, InvalidMoveException
from levelup.map import GameMap, Direction
from levelup.position import Position
from typing import Tuple


class TestCharacter(TestCase):
    def test_init(self):
        expected_name = "arbitrary"
        testobj_char = Character(expected_name)
        self.assertEqual(testobj_char.name, expected_name)
        expected_position = None
        self.assertEqual(testobj_char.position, expected_position)
    
    def test_enter_map(self):
        expected_name = "arbitrary"
        testobj_char = Character(expected_name)
  #      coordinates = None
        fakeGameMap = GameMap
        testobj_char.enter_map(fakeGameMap)
        testobj = Position(0, 1)
        expected_position = Position(0, 1)
        self.assertEqual(expected_position, testobj)

    def test_move(self):
        position = 6,6
        expected_name = "arbitrary"
        testobj_char = Character(expected_name)
        testobj_char_test_move = Character.FakeMove("N")

        #self.assertEqual(testobj_char.position, tuple(6,5))
