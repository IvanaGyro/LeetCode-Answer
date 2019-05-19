class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        table = {(r, c) for r in range(R) for c in range(C)}
        table = sorted(list(table), key=lambda x: x[0] + x[1])
        ans = []
        for i, j in table:
            if r0 >= i and c0 >= j:
                ans.append([r0-i, c0-j])
            if j > 0 and r0 >= i and c0 + j < C:
                ans.append([r0-i, c0+j])
            if i > 0 and r0 + i < R and c0 >= j:
                ans.append([r0+i, c0-j])
            if i > 0 and j > 0 and r0 + i < R and c0 + j < C:
                ans.append([r0+i, c0+j])

        return ans