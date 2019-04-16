class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        import bisect
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        col = [row[0] for row in matrix]
        c_idx = bisect.bisect(col, target)
        if c_idx > len(matrix) or c_idx == 0:
            return False
        c_idx -= 1
        r_idx = bisect.bisect_left(matrix[c_idx], target)
        if r_idx >= len(matrix[0]) or matrix[c_idx][r_idx] != target:
            return False
        return True