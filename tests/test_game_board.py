import unittest
from game_engine.board_game import BoardGame

class GameBoardTestCase(unittest.TestCase):
    def setUp(self):
        self.SIZE_RAW = 3
        self.SIZE_COLUMNE = 3
        self.board_game = BoardGame(self.SIZE_RAW, self.SIZE_COLUMNE)

    def tearDown(self):
        pass

    def test_size(self):
        size_board = 0
        for raw in self.board_game.board_game:
            size_board += len(raw)

        self.assertEqual(
            self.SIZE_RAW * self.SIZE_COLUMNE,
            size_board
        )

    def test_draw_pixel(self):
        x = 0
        y = 0
        representation_before_draw = '0'
        representation_after_draw = 'x'
        pixel = (x, y, representation_after_draw)

        self.assertEqual(
            self.board_game.board_game[x][y],
            representation_before_draw
        )

        self.board_game.draw_pixel(pixel)

        self.assertEqual(
            self.board_game.board_game[x][y],
            representation_after_draw
        )

    def test_draw_pixels(self):
        first_raw = 0
        representation_before_draw = '0'
        representation_after_draw = 'x'

        pixels = [
            (0, 0, representation_after_draw),
            (0, 1, representation_after_draw),
            (0, 2, representation_after_draw)
        ]

        for y in range(self.SIZE_COLUMNE):
            self.assertEqual(
                self.board_game.board_game[first_raw][y],
                representation_before_draw
            )

        self.board_game.draw_pixels(pixels)

        for y in range(self.SIZE_COLUMNE):
            self.assertEqual(
                self.board_game.board_game[first_raw][y],
                representation_after_draw
            )

    def test_move_pixel(self):
        x = 1
        y = 1
        representation_before = '0'
        representation_after = 'x'
        pixel = (x, y, representation_after)

        for y in range(1,3):
            self.assertEqual(
                self.board_game.board_game[x][y],
                representation_before
            )

        self.board_game.draw_pixel(pixel)

        self.assertEqual(
            self.board_game.board_game[x][1],
            representation_after
        )

        self.assertEqual(
            self.board_game.board_game[x][2],
            representation_before
        )

        self.board_game.move_pixel(
            (1,1, representation_after),
            (1,2, representation_before)
        )

        self.assertEqual(
            self.board_game.board_game[x][1],
            representation_before
        )

        self.assertEqual(
            self.board_game.board_game[x][2],
            representation_after
        )