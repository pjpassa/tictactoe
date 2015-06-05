import random
import sys
from board import Board, import_tic_tac_toe_board
import board_evaluator


def debug_print(information):
    print("DEBUG: ", information, file=sys.stderr)

player, text_board = import_tic_tac_toe_board()

board = Board(text_board)
coords = (1, 1)
while True:
    coords = (random.randint(0, 2), random.randint(0, 2))
    if board.get_value(coords) == "_":
        break

print('{} {}'.format(coords[0], coords[1]))
