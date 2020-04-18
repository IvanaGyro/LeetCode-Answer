class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        mask = 1
        for i in range(32):
            ans <<= 1
            ans |= (n & mask) >> i
            mask <<= 1
        return ans
    