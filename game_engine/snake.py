
class Snake:

    def __init__(self):
        self.head = (0, 3, '0')
        self.body = [
            (0, 2, '0'),
            (0, 1, '0')
        ]
        self.tail = (0, 0, '0')

    def move(self, next_spot):
        self.body.append(self.head)
        self.head = next_spot
        self.tail = self.body.pop(0)


