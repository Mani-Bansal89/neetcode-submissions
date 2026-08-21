class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_set = set()
            col_set = set()
            block_set = set()
            for j in range(9):
                if (board[i][j] != "."):
                    if (board[i][j] in row_set):
                        return False
                    row_set.add(board[i][j])
                if (board[j][i] != "."):
                    if (board[j][i] in col_set):
                        return False
                    col_set.add(board[j][i])
                p = (i // 3) * 3 + j // 3
                q = (i % 3) * 3 + j % 3
                if (board[p][q] != "."):
                    if (board[p][q] in block_set):
                        return False
                    block_set.add(board[p][q])

        return True