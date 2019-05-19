class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        m = c - b
        n = b - a
        if m == 2 or n == 2:
            min = 1
        else:
            min = (m != 1) + (n != 1)
        return [min, m + n - 2]
    