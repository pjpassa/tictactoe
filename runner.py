import sys
from subprocess import Popen, PIPE

X = 'X'
O = 'O'
PLAYERS = [X, O]
BOARD = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_'],
]


def is_game_over():
    if player_wins(X) or player_wins(O) or is_cat_game():
        return True


def player_wins(player):
    if column_win(player) or row_win(player) or diagonal_win(player):
        return True


def is_cat_game():
    cat_game = True
    for row in BOARD:
        for cell in row:
            if cell == '_':
                cat_game = False
    return cat_game


def column_win(player):
    for col in range(3):
        if all([BOARD[row][col] == player for row in range(3)]):
            return True


def row_win(player):
    for row in BOARD:
        if [player] * 3 == row:
            return True


def diagonal_win(player):
    if BOARD[0][2] == player and BOARD[1][1] == player and BOARD[2][0] == player:
        return True
    if BOARD[0][0] == player and BOARD[1][1] == player and BOARD[2][2] == player:
        return True


def print_board():
    board = [" ".join(row) for row in BOARD]
    board = ["  A B C",
             "1 " + board[0],
             "2 " + board[1],
             "3 " + board[2]]
    for row in board:
        print(row)


def get_board_string():

    def get_rows():
        for row in BOARD:
            yield ''.join(row)

    return '\n'.join(list(get_rows()))


def turn(player, bot):
    print_board()
    row = -1
    column = -1
    if bot in ["player", "person"]:
        print("You are {}'s'.".format(player))
        while True:
            cell = input("Input grid letter first. > ").lower()
            if cell[0] in "abc" and cell[1] in "123":
                break
        row = int(cell[1]) - 1
        column = "abc".index(cell[0])
    else:
        p = Popen(['python', bot], stdout=PIPE, stdin=PIPE)
        output = p.communicate(input=bytes("{}\n{}".format(player, get_board_string()), encoding="utf-8"))[0]
        row, column = map(int, output.strip().split(bytes(' ', encoding="utf-8")))
    if BOARD[row][column] != '_':
        raise Exception("row: {} column: {} is an illegal move".format(row, column))
    BOARD[row][column] = player
    print("\n------------------------\n")


if __name__ == '__main__':

    x_bot = sys.argv[1]
    o_bot = sys.argv[2]

    current_player = 0
    bots = {X: x_bot, O: o_bot}
    while not is_game_over():
        turn(PLAYERS[current_player], bots[PLAYERS[current_player]])
        current_player = 1 if current_player == 0 else 0
    print_board()
