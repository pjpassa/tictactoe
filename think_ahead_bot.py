import sys
import random
from board import Board, import_tic_tac_toe_board
import board_evaluator as be


def debug_print(information):
    print("DEBUG: ", information, file=sys.stderr)


def good_move(board, player, coords):
    debug_print("Evaluating {} for {}.".format(coords, player))
    if player == "X":
        opponent = "O"
    else:
        opponent = "X"
    wins = be.victory_chances(board)
    my_wins = [coordinates for team, coordinates in wins if team == player]
    their_wins = [coordinates for team, coordinates in wins if team != player]
    if my_wins:
        if coords in my_wins:
            debug_print("Win in one for me!")
            return True
        debug_print("I would miss a win in one for me!")
        return False
    if their_wins:
        if coords in their_wins:
            debug_print("I am blocking a win in one!")
            return True
        debug_print("I would miss blocking a win in one for them!")
        return False
    debug_print("No immediate wins.")
    debug_print(my_wins)
    if len(my_wins) >= 2:
        debug_print("I have two win possibilities!")
        return True
    if len(their_wins) >= 2:
        debug_print("I would have two loss possibilities.")
        return False
    new_board = board.make_move(player, coords)
    new_board_empty_squares = new_board.get_empty_squares()
    random.shuffle(new_board_empty_squares)
    potential_moves = []
    for square in new_board_empty_squares:
        debug_print("Stepping in to {}.".format(square))
        if not good_move(new_board, opponent, square):
            potential_moves.append(square)
        debug_print("Stepping out of {}.".format(square))
    if potential_moves:
        debug_print("Good move.")
        return True
    debug_print("Bad move.")
    return False


def look_ahead(board, player, move):
    new_board = board.make_move(player, move)
    wins = be.victory_chances(new_board)
    my_wins = [coordinates for team, coordinates in wins if team == player]
    if len(my_wins) >= 2:
        return True
    if player == "X":
        opponent = "O"
    else:
        opponent = "X"
    empty_squares = new_board.empty_squares()
    if all([not look_ahead(new_board, opponent, move) for move in empty_squares]):
        return True
    return False

player, board_text = import_tic_tac_toe_board()
board = Board(board_text)
choices = board.get_empty_squares()
random.shuffle(choices)

# need to evaluate all moves, then pick one, which means I need to assign values to moves
# need a fucntion to check for win in one.  Then I need a function to evaluate next position (are there two wins for me or two wins for them)

good_moves = []
while choices:
    move = choices.pop()
    if good_move(board, player, move):
        good_moves.append(move)

move = random.choice(good_moves)

print("{} {}".format(move[0], move[1]))
