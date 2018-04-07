import unittest
from game_engine.snake import Snake


class SnakeTestCase(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()

    def tearDown(self):
        pass

    def test_snake_init(self):
        tail = (1, 1)
        body = [
            (1, 2),
            (1, 3),
        ]
        head = (1, 4)

        self.assertEqual(
            head,
            self.snake.head
        )

        self.assertEqual(
            body,
            self.snake.body
        )

        self.assertEqual(
            tail,
            self.snake.tail
        )

    def test_snake_move_right(self):
        tail = (1, 2)
        body = [
            (1, 3),
            (1, 4)
        ]
        head = (1, 5)

        direction_right = (1, 5)

        self.snake.move(direction_right)

        self.assertEqual(
            head,
            self.snake.head
        )

        self.assertEqual(
            body,
            self.snake.body
        )

        self.assertEqual(
            tail,
            self.snake.tail
        )

    def test_snake_move_down(self):
        tail = (1, 2)
        body = [
            (1, 3),
            (1, 4)
        ]
        head = (2, 4)

        direction_down = (2, 4)

        self.snake.move(direction_down)

        self.assertEqual(
            head,
            self.snake.head
        )

        self.assertEqual(
            body,
            self.snake.body
        )

        self.assertEqual(
            tail,
            self.snake.tail
        )

    def test_snake_move_up(self):
        tail = (1, 2)
        body = [
            (1, 3),
            (1, 4)
        ]
        head = (0, 4)
        direction_up = (0, 4)

        self.snake.move(direction_up)

        self.assertEqual(
            head,
            self.snake.head
        )

        self.assertEqual(
            body,
            self.snake.body
        )

        self.assertEqual(
            tail,
            self.snake.tail
        )

    def test_snake_move_left(self):
        tail = (1, 3)
        body = [
            (1, 4),
            (2, 4)
        ]
        head = (2, 3)

        direction_down = (2, 4)
        direction_left = (2, 3)

        self.snake.move(direction_down)
        self.snake.move(direction_left)

        self.assertEqual(
            head,
            self.snake.head
        )

        self.assertEqual(
            body,
            self.snake.body
        )

        self.assertEqual(
            tail,
            self.snake.tail
        )
