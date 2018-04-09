from game_engine.keyboard_driver import Keyboard
from game_engine.board_game import BoardGame


class Snake:

    def __init__(self, size_raw=6, size_columne=6):
        self.tail = (1, 1)
        self.body = [(1, 2), (1, 3)]
        self.head = (1, 4)
        self.keyboard = Keyboard()
        self.board_game = BoardGame(size_raw, size_columne)

    def __str__(self):
        return str([self.tail] + self.body + [self.head])

    def __iter__(self):
        for part_snake in ([self.tail] + self.body + [self.head]):
            yield part_snake

    def __next__(self):
        return self

    def __len__(self):
        return len([self.tail] + self.body + [self.head])

    def move(self, next_spot):
        self.body.append(self.head)
        self.head = next_spot
        self.tail = self.body.pop(0)

    def map_key_value_on_direction(self, key_value):
        direction = {
            b"\x1b[A": 'up',
            b"\x1b[B": 'down',
            b"\x1b[C": 'right',
            b"\x1b[D": 'left',
            b'\x03\x03\x03': 'exit'
        }
        return direction.get(key_value, 'Wrong key')

    def change_direction(self):
        key_value = self.keyboard.get_key_value()
        direction = self.map_key_value_on_direction(key_value)
        x, y = self.head

        if 'up' == direction:
            x -= 1
        elif 'down' == direction:
            x += 1
        elif 'right' == direction:
            y += 1
        elif 'left' == direction:
            y -= 1

        self.move((x, y))
