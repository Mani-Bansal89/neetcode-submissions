class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in seen:
                    return False
                elif board[i][j] != '.':
                    seen.add(board[i][j])
            

        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] != '.' and board[j][i] in seen:
                    return False
                elif board[j][i] != '.':
                    seen.add(board[j][i])
            
        for i in range(0,9,3):
            for j in range(0,9,3):
                seen = set()
                for k in range(3):
                    for l in range(3):
                        print(board[i+k][j+l])
                        if board[i+k][j+l] != '.' and board[i+k][j+l] in seen:
                            return False
                        elif board[i+k][j+l] != '.':
                            seen.add(board[i+k][j+l])
        return True



