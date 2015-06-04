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
        col_start = 2*diag_number
        col_inc = -1**diag_number
        return [self.board[i][col_start + i*col_inc] for i in range(2)]

    @property
    def text_state(self):
        return [''.join(row) for row in self.board]

    def detect_victory_chance(self, set):
        if set[0] == set[1] or set[0] == set[2]:
            return set[0]
        elif set[1] == set[2]:
            return set[1]
        return "_"

    def row_victory_chance(self, row_number):
        return(self.detect_victory_chance(self.board.get_row(row_number)))

    def col_victory_chance(self, col_number):
        return(self.detect_victory_chance(self.board.get_col(col_number)))

    def diag_victory_chance(self, diag_number):
        return(self.detect_victory_chance(self.board.get_diag(diag_number)))
