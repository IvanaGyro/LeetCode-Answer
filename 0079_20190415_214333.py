class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        
        def find(x, y, off):
            nonlocal word
            if off == len(word):
                return True
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                return False
            if board[x][y] == word[off]:
                cache = board[x][y]
                board[x][y] = None
                if find(x-1, y, off+1) or find(x, y-1, off+1) or find(x+1, y, off+1) or find(x, y+1, off+1):
                    return True
                board[x][y] = cache
            return False
        
        fisrt_c = word[0]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if find(i, j, 0):
                    return True
        return False
                        
        

                    