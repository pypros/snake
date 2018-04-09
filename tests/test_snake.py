from unittest import TestCase
from unittest.mock import Mock
from game_engine.snake import Snake


class SnakeTestCase(TestCase):
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

    def test_snake_prevent_backward_movement_false(self):
        next_spot = (1, 4)
        self.assertFalse(self.snake.prevent_backward_movement(next_spot))

    def test_snake_prevent_backward_movement_true(self):
        next_spot = (1, 5)
        self.assertTrue(self.snake.prevent_backward_movement(next_spot))

    def test_snake_check_border_up(self):
        tail = (1, 2)
        body = [
            (1, 3),
            (1, 4)
        ]
        head = (0, 4)

        self.snake.keyboard._Keyboard__get_key_value = Mock(side_effect=['\x1b[A','\x1b[A'])
        self.snake.change_direction()
        self.snake.change_direction()

        self.assertEqual(
            tail,
            self.snake.tail
        )

        self.assertEqual(
            body,
            self.snake.body
        )

        self.assertEqual(
            head,
            self.snake.head
        )
    def test_snake_check_border_down(self):
        tail = (2, 4)
        body = [
            (3, 4),
            (4, 4)
        ]
        head = (5, 4)

        self.snake.keyboard._Keyboard__get_key_value = Mock(side_effect=['\x1b[B','\x1b[B', '\x1b[B','\x1b[B'])

        self.snake.change_direction()
        self.snake.change_direction()
        self.snake.change_direction()
        self.snake.change_direction()

        self.assertEqual(
            tail,
            self.snake.tail
        )

        self.assertEqual(
            body,
            self.snake.body
        )

        self.assertEqual(
            head,
            self.snake.head
        )

    def test_snake_check_border_right(self):
        tail = (1, 2)
        body = [
            (1, 3),
            (1, 4)
        ]
        head = (1, 5)

        self.snake.keyboard._Keyboard__get_key_value = Mock(side_effect=['\x1b[C','\x1b[C'])
        self.snake.change_direction()
        self.snake.change_direction()

        self.assertEqual(
            tail,
            self.snake.tail
        )

        self.assertEqual(
            body,
            self.snake.body
        )

        self.assertEqual(
            head,
            self.snake.head
        )

    def test_snake_check_border_left(self):
        tail = (2, 3)
        body = [
            (2, 2),
            (2, 1)
        ]
        head = (2, 0)

        self.snake.keyboard._Keyboard__get_key_value = Mock(side_effect=[
            '\x1b[B',
            '\x1b[D',
            '\x1b[D',
            '\x1b[D',
            '\x1b[D',
            '\x1b[D'
        ])
        self.snake.change_direction()
        self.snake.change_direction()
        self.snake.change_direction()
        self.snake.change_direction()
        self.snake.change_direction()
        self.snake.change_direction()

        self.assertEqual(
            tail,
            self.snake.tail
        )

        self.assertEqual(
            body,
            self.snake.body
        )

        self.assertEqual(
            head,
            self.snake.head
        )

    def test_snake_map_key_value_on_direction(self):
        direction = {
            b"\x1b[A": 'up',
            b"\x1b[B": 'down',
            b"\x1b[C": 'right',
            b"\x1b[D": 'left',
            b'\x03\x03\x03': 'exit'
        }

        for key in direction:
            self.assertEqual(
                direction[key],
                self.snake.map_key_value_on_direction(key)
            )

    def test_snake_map_key_on_direction_and_move_up(self):
        tail = (1, 2)
        body = [
            (1, 3),
            (1, 4)
        ]
        head = (0, 4)
        self.snake.keyboard._Keyboard__get_key_value = Mock(return_value='\x1b[A')

        self.snake.change_direction()

        self.assertEqual(
            tail,
            self.snake.tail
        )

        self.assertEqual(
            body,
            self.snake.body
        )

        self.assertEqual(
            head,
            self.snake.head
        )

    def test_snake_map_key_on_direction_down(self):
        tail = (1, 2)
        body = [
            (1, 3),
            (1, 4)
        ]
        head = (2, 4)
        self.snake.keyboard._Keyboard__get_key_value = Mock(return_value='\x1b[B')

        self.snake.change_direction()

        self.assertEqual(
            tail,
            self.snake.tail
        )

        self.assertEqual(
            body,
            self.snake.body
        )

        self.assertEqual(
            head,
            self.snake.head
        )

    def test_snake_map_key_on_direction_right(self):
        tail = (1, 2)
        body = [
            (1, 3),
            (1, 4)
        ]
        head = (1, 5)

        self.snake.keyboard._Keyboard__get_key_value = Mock(return_value='\x1b[C')
        self.snake.change_direction()

        self.assertEqual(
            tail,
            self.snake.tail
        )

        self.assertEqual(
            body,
            self.snake.body
        )

        self.assertEqual(
            head,
            self.snake.head
        )

    def test_snake_map_key_on_direction_left(self):
        tail = (1, 3)
        body = [
            (1, 4),
            (2, 4)
        ]
        head = (2, 3)
        self.snake.keyboard._Keyboard__get_key_value = Mock(return_value='\x1b[B')
        self.snake.change_direction()

        self.snake.keyboard._Keyboard__get_key_value = Mock(return_value='\x1b[D')
        self.snake.change_direction()

        self.assertEqual(
            tail,
            self.snake.tail
        )

        self.assertEqual(
            body,
            self.snake.body
        )

        self.assertEqual(
            head,
            self.snake.head
        )

    def test_snake_magic_method_str(self):
        snake_string_representation = "[(1, 1), (1, 2), (1, 3), (1, 4)]"
        self.assertEqual(
            snake_string_representation,
            str(self.snake)
        )

    def test_snake_magic_method_iter(self):
        tail = (1, 1)
        it = iter(self.snake)
        self.assertEqual(
            tail,
            next(it)
        )

    def test_snake_magic_method_len(self):
        init_length_snake = 4
        self.assertEqual(
            init_length_snake,
            len(self.snake)
        )