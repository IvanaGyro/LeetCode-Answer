class Solution:
    def climbStairs(self, n: int) -> int: 
        if n <= 1:
            return 1
        prev, cur = 1, 1
        for i in range(n - 1):
            prev, cur = cur, prev + cur
        return cur
