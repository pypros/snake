from game_engine.keyboard_driver import Keyboard


class Snake:

    def __init__(self):
        self.tail = (1, 1)
        self.body = [
            (1, 2),
            (1, 3)
        ]
        self.head = (1, 4)
        self.keyboard = Keyboard()

    def move(self, next_spot):
        self.body.append(self.head)
        self.head = next_spot
        self.tail = self.body.pop(0)

    def change_direction(self):
        key_value = self.keyboard.get_key_value()
        direct = {
            b"\x1b[A": "up",
            b"\x1b[B": "down",
            b"\x1b[C": "right",
            b"\x1b[D": "left"
        }
        return direct[key_value]
