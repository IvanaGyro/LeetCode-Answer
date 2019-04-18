class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1] * (rowIndex + 1)
        for i in range(rowIndex - 1):
            for j in range(i, -1, -1):
                res[j + 1] += res[j]
        return res