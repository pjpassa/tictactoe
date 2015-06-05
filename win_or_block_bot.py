import random
from board import Board, import_tic_tac_toe_board
import board_evaluator as be


player, text_board = import_tic_tac_toe_board()
board = Board(text_board)
corners = [(0, 2), (0, 0), (2, 0), (2, 2)]
random.shuffle(corners)
coords = (1, 1)

while board.get_value(coords) != "_":
    if corners:
        coords = corners.pop()
    else:
        coords = (random.randint(0, 2), random.randint(0, 2))

wins = be.victory_chances(board)
my_wins = [coordinates for team, coordinates in wins if team == player]
their_wins = [coordinates for team, coordinates in wins if team != player]
if their_wins:
    coords = their_wins.pop()
if my_wins:
    coords = my_wins.pop()

print('{} {}'.format(coords[0], coords[1]))
