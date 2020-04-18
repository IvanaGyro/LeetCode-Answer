class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        base = 10
        cnt = 0
        while base <= n:
            cnt += 1
            base *= 10
        if cnt == 0:
            return 1
        base //= 10
        hi = n // base
        lo = n % base
        res = cnt * (hi * 10**(cnt-1))
        if hi > 1:
            res += 10**cnt
        elif hi == 1:
            res += lo + 1
        return res + self.countDigitOne(lo)
    