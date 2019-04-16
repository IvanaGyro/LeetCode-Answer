class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        for y in range(len(matrix) >> 1):
            for x in range(y, len(matrix) - 1 - y):
                matrix[y][x], matrix[x][l-y-1], matrix[l-y-1][l-x-1], matrix[l-x-1][y] = matrix[l-x-1][y], matrix[y][x], matrix[x][l-y-1], matrix[l-y-1][l-x-1]