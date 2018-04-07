
class Snake:

    def __init__(self):
        self.tail = (1, 1)
        self.body = [
            (1, 2),
            (1, 3)
        ]
        self.head = (1, 4)

    def move(self, next_spot):
        self.body.append(self.head)
        self.head = next_spot
        self.tail = self.body.pop(0)
