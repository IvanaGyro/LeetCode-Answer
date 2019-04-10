class Solution:
    def myPow(self, x: float, n: int) -> float:
        mask = 1 << 31
        if n == ~(mask-1):
            overflow = True
        else:
            overflow = False
        if n < 0:
            neg = True
            if overflow:
                n = -(n+1)
            else:
                n = -n
        else:
            neg = False
        
        ans = 1.
        while mask:
            ans *= ans
            if mask & n:
                ans *= x
            mask >>= 1
        
        if neg:
            if overflow:
                return 1 / ans / x
            else:
                return 1 / ans
        else:
            return ans
        