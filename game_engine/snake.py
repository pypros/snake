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

    def change_direction(self):
        '''
        Key value
            b'\x1b[A' -> 'up'
            b'\x1b[B' -> 'down'
            b'\x1b[C' -> 'right'
            b'\x1b[D' -> 'left'
        '''

        key_value = self.keyboard.get_key_value()
        x, y = self.head

        if b"\x1b[A" == key_value:
            x -= 1
        elif b"\x1b[B" == key_value:
            x += 1
        elif b"\x1b[C" == key_value:
            y += 1
        elif b"\x1b[D" == key_value:
            y -= 1

        self.move((x, y))

