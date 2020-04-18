class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        l, r = 0, len(matrix[0]) - 1
        while l < r:
            m = (l + r) // 2
            if matrix[0][m] > target:
                r = m - 1
            elif matrix[0][m] == target:
                return True
            else:
                l = m + 1
        x = r
        if r < 0:
            return False
        if matrix[0][x] == target:
            return True
        l, r = 0, len(matrix) - 1
        while l < r:
            m = (l + r) // 2
            if matrix[m][x] > target:
                r = m - 1
            elif matrix[m][x] == target:
                return True
            else:
                l = m + 1
        return matrix[l][x] == target