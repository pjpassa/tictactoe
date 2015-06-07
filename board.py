def import_tic_tac_toe_board():
    return (input(), [input(), input(), input()])


class Board:
    def __init__(self, text_state):
        self.board = [[value for value in row] for row in text_state]

    def get_value(self, coordinates):
        return self.board[coordinates[0]][coordinates[1]]

    def get_row(self, row_number):
        return self.board[row_number]

    def get_col(self, col_number):
        return [row[col_number] for row in self.board]

    def get_diag(self, diag_number):
        return [self.get_value(self.get_coord_diag(diag_number, i))
                for i in range(3)]

    def get_coord_diag(self, diag_number, index):
        return (index, 2 * diag_number + index * (-1)**diag_number)

    def make_move(self, player, coordinates):
        current_board = self.board[:]
        current_board[coordinates[0]][coordinates[1]] = player
        return Board(current_board)

    def get_empty_squares(self):
        squares = []
        for row_num, row in enumerate(self.board):
            for col_num, col in enumerate(row):
                if col == "_":
                    squares.append((row_num, col_num))
        return squares

    @property
    def text_state(self):
        return [''.join(row) for row in self.board]
