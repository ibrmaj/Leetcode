class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            row_dict = {str(x): 0 for x in range(1, 10)}
            for i in row:
                if i != '.':
                    row_dict[i] += 1
            if any(value > 1 for value in row_dict.values()):
                return False

        # Check columns
        for j in range(len(board[0])):
            col_dict = {str(x): 0 for x in range(1, 10)}
            for i in range(len(board)):
                if board[i][j] != '.':
                    col_dict[board[i][j]] += 1
            if any(value > 1 for value in col_dict.values()):
                return False

        # Check subboxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                subbox_dict = {str(x): 0 for x in range(1, 10)}
                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        if board[i][j] != '.':
                            subbox_dict[board[i][j]] += 1
                if any(value > 1 for value in subbox_dict.values()):
                    return False

        return True
