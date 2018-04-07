from game_engine.keyboard_driver import Keyboard

from unittest import TestCase
from unittest.mock import Mock


class KeyboardTestCase(TestCase):
    def setUp(self):
        self.keyboard = Keyboard()

    def tearDown(self):
        pass

    def test_keyboard_get_key_value_right_arrow(self):
        self.keyboard._Keyboard__get_key_value = Mock(return_value='\x1b[A')
        pressed_key = self.keyboard.get_key_value()
        self.keyboard._Keyboard__get_key_value.assert_any_call()
        self.assertEqual(
            b'\x1b[A',
            pressed_key
        )

    def test_keyboard_get_key_value_char(self):
        self.keyboard.data_buffer_length = 1
        self.keyboard._Keyboard__get_key_value = Mock(return_value='a')
        self.keyboard.get_key_value()
        self.keyboard._Keyboard__get_key_value.assert_any_call()
        self.assertEqual(
            b'a',
            self.keyboard.key_value
        )
