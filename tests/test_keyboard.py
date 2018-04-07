from game_engine.keyboard_driver import Keyboard

from unittest import TestCase
from unittest.mock import Mock


class KeyboardTestCase(TestCase):
    def setUp(self):
        self.keyboard = Keyboard()

    def tearDown(self):
        pass

    def test_keyboard_get(self):
        self.keyboard._Keyboard__get_key_value = Mock(return_value='\x1b[A')
        self.keyboard.get()
        self.keyboard._Keyboard__get_key_value.assert_any_call()
        self.assertEqual(
            b'\x1b[A',
            self.keyboard.key_value
        )

    def test_keyboard_direction_up(self):
        self.keyboard.key_value = b'\x1b[A'
        self.assertEqual(
            'up',
            self.keyboard.direction()
        )

    def test_keyboard_direction_right(self):
        self.keyboard.key_value = b'\x1b[C'
        self.assertEqual(
            'right',
            self.keyboard.direction()
        )

    def test_keyboard_direction_left(self):
        self.keyboard.key_value = b'\x1b[D'
        self.assertEqual(
            'left',
            self.keyboard.direction()
        )
    def test_keyboard_direction_down(self):
        self.keyboard.key_value = b'\x1b[B'
        self.assertEqual(
            'down',
            self.keyboard.direction()
        )

    def test_keyboard_direction_right(self):
        self.keyboard.key_value = b'\x1b[C'
        self.assertEqual(
            'right',
            self.keyboard.direction()
        )

    def test_keyboard_direction_left(self):
        self.keyboard.key_value = b'\x1b[D'
        self.assertEqual(
            'left',
            self.keyboard.direction()
        )
