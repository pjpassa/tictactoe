import sys
import random
from board import Board, import_tic_tac_toe_board
import board_evaluator as be


def get_opponent(player):
    if player == "X":
        return "O"
    return "X"


def good_move(board, player, coords):
    opponent = get_opponent(player)
    wins = be.victory_chances(board)
    my_wins = [coordinates for team, coordinates in wins if team == player]
    their_wins = [coordinates for team, coordinates in wins if team != player]
    if my_wins:
        if coords in my_wins:
            return 10
        return -10
    if their_wins:
        if coords in their_wins:
            return 3
        return -3
    return look_ahead(board, player, coords)


def look_ahead(board, player, move):
    new_board = board.make_move(player, move)
    wins = be.victory_chances(new_board)
    my_wins = [coordinates for team, coordinates in wins if team == player]
    if len(my_wins) >= 2:
        return 2
    opponent = get_opponent(player)
    if my_wins:
        return -look_ahead(new_board, opponent, my_wins[0])
    empty_squares = new_board.get_empty_squares()
    if empty_squares:
        new_moves = [-look_ahead(new_board, opponent, move)
                     for move in empty_squares]
        return min(new_moves)
    return 1


player, board_text = import_tic_tac_toe_board()
board = Board(board_text)
choices = board.get_empty_squares()
random.shuffle(choices)

good_moves = []
if len(choices) == 9:
    good_moves.append((7, random.choice(choices)))
else:
    while choices:
        move = choices.pop()
        score = good_move(board, player, move)
        good_moves.append((score, move))

good_moves = sorted(good_moves, key=lambda x: x[0])
move = good_moves.pop()[1]

print("{} {}".format(move[0], move[1]))
