from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return 0
        for n, t in Counter(nums).items():
            if t > len(nums) >> 1:
                return n
            