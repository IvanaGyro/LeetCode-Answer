class Solution:
    def trailingZeroes(self, n: int) -> int:
        twos = 0
        tmp = n
        while tmp:
            tmp >>= 1
            twos += tmp
        fives = 0
        tmp = n
        while tmp:
            tmp //= 5
            fives += tmp
        return min(twos, fives)
    