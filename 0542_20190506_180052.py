from collections import deque
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return matrix
        tb = [[False]*len(matrix[0]) for _ in range(len(matrix))]
        
        next = deque()
        def flood_zero(x, y):
            if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
                return
            if not tb[x][y]:
                tb[x][y] = True
                if matrix[x][y] != 0:
                    next.append((x, y))
                else:
                    flood_zero(x-1, y)
                    flood_zero(x+1, y)
                    flood_zero(x, y-1)
                    flood_zero(x, y+1)
        
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y] == 0:
                    flood_zero(x, y)
        
        cur = 1
        while next:
            for _ in range(len(next)):
                x, y = next.popleft()
                for x_, y_ in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if 0 <= x_ < len(matrix) and 0 <= y_ < len(matrix[0]) and not tb[x_][y_]:
                        tb[x_][y_] = True
                        matrix[x_][y_] = cur + 1
                        next.append((x_, y_))
            cur += 1
        
        return matrix
        