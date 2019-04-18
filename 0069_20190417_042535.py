class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        cur, prev = x, 0
        while True:
            prev, cur = cur, (cur + x / cur) / 2
            # prev, cur = cur, (cur*cur*(cur*cur+6*x)+x*x)/(4*cur*(cur*cur+x))
            if prev - cur < 0.1:
                break
        return int(cur)
