class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        counts = [[None]*9, [None]*9, [None]*9]
        for i in range(0, 3):
            for j in range(0, 9):
                counts[i][j] = [1]*9
        
        for r in range(0, 9):
            for c in range(0, 9):
                if board[r][c] == '.':
                    continue
                num = int(board[r][c])-1
                if counts[0][r][num] == 0 or counts[1][c][num] == 0 \
                        or counts[2][c//3*3 + r//3][num] == 0:
                    return False
                counts[0][r][num] = 0
                counts[1][c][num] = 0 
                counts[2][c//3*3 + r//3][num] = 0
        return True