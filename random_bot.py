import random
import sys
from board import Board, import_tic_tac_toe_board
import board_evaluator


def debug_print(information):
    print("DEBUG: ", information, file=sys.stderr)

board = Board(import_tic_tac_toe_board()[1])
#debug_print(board.text_state)
coords = (1, 1)
while True:
    coords = (random.randint(0, 2), random.randint(0, 2))
    if board.get_value(coords) == "_":
        break

#debug_print("{} {}".format(coords[0], coords[1]))
print('{} {}'.format(coords[0], coords[1]))
