from math import floor
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        n = len(nums)
        min_ = min(nums)
        max_ = max(nums)
        rng = max_ - min_
        if rng <= 1:
            return rng
        
        INT_MAX = (1 << 32) - 1
        buckets = [[] for _ in range(n)]
        for num in nums:
            key = (num - min_) * (n - 1) // rng
            if not buckets[key]:
                buckets[key] = [num, num]
            else:
                lo, hi = buckets[key]
                buckets[key] = [min(lo, num), max(hi, num)]
            
        lo, hi = buckets[0]
        max_gap = 1
        for b in buckets[1:]:
            if b:
                max_gap = max(b[0] - hi, max_gap)
                lo, hi = b
        return max_gap
            