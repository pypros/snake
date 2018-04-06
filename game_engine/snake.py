
class Snake:

    def __init__(self):
        self.tail = (1, 1, 'x')
        self.body = [
            (1, 2, 'x'),
            (1, 3, 'x')
        ]
        self.head = (1, 4, 'x')

    def move(self, next_spot):
        self.body.append(self.head)
        self.head = next_spot
        self.tail = self.body.pop(0)


