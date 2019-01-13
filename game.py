from game_engine.console_board_game import BoardGameConsole
from game_engine.snake import Snake
import sys
import os

SIZE_RAW = 6
SIZE_COLUMNE = 6
snake = Snake()

while True:
    snake.board_game.clean()
    for x, y in snake:
        snake.board_game.draw_pixel((x, y, 'x'))
    snake.board_game.draw_pixel((*snake.food, 'T'))
    os.system('clear')
    print('Score: {}'.format(len(snake)-4))
    snake.board_game.print_game()
    snake.change_direction()
    if snake.keyboard.key_value == b'\x03\x03\x03':
        sys.exit()