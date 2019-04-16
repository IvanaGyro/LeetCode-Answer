class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m -= 1
        n -= 1
        def level(upper, lower):
            num = 1
            for i in range(lower, upper+1):
                num *= i
            return num
        min_l = min(m, n)
        return level(m + n, m + n - min_l + 1) // level(min_l, 1)