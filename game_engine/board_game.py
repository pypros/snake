class BoardGame:
    """
        BoardGame

        pixel represenation (x, y, char)
    """
    def __init__(self, size_raw, size_column):
        self.size_raw = size_raw
        self.size_column = size_column
        self.board_game = [["0" for raw_number in range(self.size_raw)] for columne_number in range(self.size_column)]

    def clean(self):
        self.board_game = [["0" for raw_number in range(self.size_raw)] for columne_number in range(self.size_column)]

    def print_game(self):
        first_row = slice(1)
        len_row = len(*self.board_game[first_row])
        print(['-'] * (len_row + 2))

        for raw in self.board_game:
            print(['-'] + raw + ['-'])

        print(['-'] * (len_row + 2))

    def draw_pixel(self, pixel):
        x, y, representation = pixel
        self.board_game[x][y] = representation

    def draw_pixels(self, pixels):
        for x, y, representation in pixels:
            self.board_game[x][y] = representation

    def move_pixel(self, current_pixel, next_pixel):
        cx, cy, _ = current_pixel
        nx, ny, _ = next_pixel
        self.board_game[cx][cy], self.board_game[nx][ny] = self.board_game[nx][ny], self.board_game[cx][cy]