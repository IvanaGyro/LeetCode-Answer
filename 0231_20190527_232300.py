class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return not (not n or n & n-1)
    