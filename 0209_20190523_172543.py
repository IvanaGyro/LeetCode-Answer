class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if s == 0:
            return 0
        
        total = 0
        n = len(nums)
        for i in range(n):
            total += nums[i]
            if total >= s:
                break
        else:
            return 0
        
        min_sub = r = i + 1
        for l in range(n):
            while total < s and r < n:
                total += nums[r]
                r += 1
            if total < s:
                return min_sub
            min_sub = min(min_sub, r-l)
            total -= nums[l]
        return min_sub
        