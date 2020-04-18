class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        w, h = len(matrix[0]), len(matrix)
        record = [(0, 0, 0)] * (len(matrix[0])+1)
        max_area = 0
        prev = 0
        for y in range(h):
            for x in range(w):
                tmp = record[x+1][0]
                if matrix[y][x] == '0':
                    record[x+1] = (0, 0, 0)
                else:
                    y_1 = record[x+1][1] + 1
                    x_1 = record[x][2] + 1
                    xy_1 = min(prev+1, y_1, x_1)
                    record[x+1] = (xy_1, y_1, x_1)
                    max_area = max(xy_1, max_area)
                prev = tmp
        return max_area**2
        