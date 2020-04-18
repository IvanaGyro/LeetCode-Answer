from math import gcd
class Solution:    
    def rotate(self, nums: List[int], k: int) -> None:
        if not nums:
            return
        n = len(nums)
        k %= n
        if k == 0:
            return           
        g = gcd(k, n)
        cycle = n // g
        for i in range(g):
            prev, j = nums[i], i + k
            for _ in range(cycle):
                prev, nums[j] = nums[j], prev
                j += k
                if j >= n:
                    j -= n
        return
