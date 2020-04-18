class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        if m == n:
            return m
        mask = 1 << 31
        ans = 0
        while mask & m ^ mask & n == 0:
            ans |= mask & m
            mask >>= 1
        return ans
    