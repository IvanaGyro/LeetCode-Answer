class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 3:
            return max(nums)
        
        def line_rob(nums):
            n = len(nums)
            dp = [None] * n
            def helper(i):
                if dp[i] is None:
                    if n - i <= 2:
                        dp[i] = max(nums[i:])
                    else:
                        dp[i] = max(nums[i]+helper(i+2), helper(i+1))
                return dp[i]
            return helper(0)
        
        return max(nums[0]+line_rob(nums[2:-1]), line_rob(nums[1:]))
    