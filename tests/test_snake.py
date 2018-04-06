import unittest
from game_engine.snake import Snake


class SnakeTestCase(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()
        self.head = (0, 3, '0')
        self.body = [
            (0, 2, '0'),
            (0, 1, '0')
        ]
        self.tail = (0, 0, '0')

    def tearDown(self):
        pass

    def test_init(self):

        self.assertEqual(
            self.head,
            self.snake.head
        )

        self.assertEqual(
            self.body,
            self.snake.body
        )

        self.assertEqual(
            self.tail,
            self.snake.tail
        )


