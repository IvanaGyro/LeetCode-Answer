class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [[False]*9 for i in range(9)]
        cols = [[False]*9 for i in range(9)]
        sqrs = [[False]*9 for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != '.':
                    n = ord(c) - ord('0') - 1
                    rows[i][n] = True
                    cols[j][n] = True
                    sqrs[i//3*3 + j//3][n] = True
        
        def find_next(i, j):
            while True:
                if i == 8 and j == 8:
                    return None
                elif j == 8:
                    i += 1
                    j = 0
                else:
                    j += 1
                if board[i][j] == '.':
                    return i, j
        
        def fill(i, j):
            # find next blank block
            next = find_next(i, j)
            if next is not None:
                ni, nj = next
            for n in range(9):
                if rows[i][n] or cols[j][n] or sqrs[i//3*3 + j//3][n]:
                    continue
                board[i][j] = str(n+1)
                rows[i][n] = cols[j][n] = sqrs[i//3*3 + j//3][n] = True
                if next is None or fill(ni, nj):
                    return True
                board[i][j] = '.'
                rows[i][n] = cols[j][n] = sqrs[i//3*3 + j//3][n] = False
            return False
                
        
        if board[0][0] == '.':
            next = (0, 0)
        else:
            next = find_next(0, 0)
            if next is None:
                return True
       
        fill(*next)