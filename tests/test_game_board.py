import unittest
from game_engine.board_game import BoardGame

class GameBoardTestCase(unittest.TestCase):
    def setUp(self):
        self.SIZE_RAW = 2
        self.SIZE_COLUMNE = 2
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