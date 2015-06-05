def detect_victory_chance(self, set):
    if set[0] == set[1] or set[0] == set[2]:
        return set[0]
    elif set[1] == set[2]:
        return set[1]
    return "_"


def row_victory_chance(self, board):
    return(self.detect_victory_chance(board.get_row(row_number)))


def col_victory_chance(self, col_number):
    return(self.detect_victory_chance(self.board.get_col(col_number)))


def diag_victory_chance(self, diag_number):
    return(self.detect_victory_chance(self.board.get_diag(diag_number)))


def victory_chances(self):
    victories = []
    for index in range(2):
        row_victory_chance
        if row_victory_chance(row_num):
            victories.append(())
