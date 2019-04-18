class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        res = [[1]]
        for _ in range(numRows - 1):
            res.append([1] + [res[-1][i] + res[-1][i - 1] for i in range(1, len(res[-1]))] + [1])
        return res