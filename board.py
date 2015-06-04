class Board:
    def __init__(self, text_state):
        self.board = [[value for value in text] for text in text_state]

    def get_value(self, coordinates):
        return self.board[coordinates[0]][coordinates[1]]

    def get_row(self, row_number):
        return self.board[row_number]

    def get_col(self, col_number):
        return [row[col_number] for row in self.board]

    def get_diag(self, diag_number):
        row_start = 0
        col_start = 2*diag_number
        row_inc = 1
        col_inc = -1**diag_number
        diag = []
        for i in range(0, 2):
            diag.append(self.board[row_start+i*row_inc][col_start+i*col_inc])
