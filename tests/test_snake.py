import unittest
from game_engine.snake import Snake


class SnakeTestCase(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()

    def tearDown(self):
        pass

    def test_init(self):
        tail = (1, 1, 'x')
        body = [
            (1, 2, 'x'),
            (1, 3, 'x'),
        ]
        head = (1, 4, 'x')

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

    def test_move_right(self):
        tail = (1, 2, 'x')
        body = [
            (1, 3, 'x'),
            (1, 4, 'x')
        ]
        head = (1, 5, 'x')

        direction_right = (1,5,'x')

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

    def test_move_down(self):
        tail = (1, 2, 'x')
        body = [
            (1, 3, 'x'),
            (1, 4, 'x')
        ]
        head = (2, 4, 'x')

        direction_down = (2,4,'x')

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

    def test_move_up(self):
        tail = (1, 2, 'x')
        body = [
            (1, 3, 'x'),
            (1, 4, 'x')
        ]
        head = (0,4,'x')

        direction_up = (0,4,'x')

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

    def test_move_left(self):
        tail = (1, 3, 'x')
        body = [
            (1, 4, 'x'),
            (2, 4, 'x')
        ]
        head = (2, 3, 'x')

        direction_down = (2,4,'x')
        direction_left = (2,3,'x')

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