class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        weights = {}
        for num in nums:
            if num not in weights:
                weights[num] = num
            else:
                weights[num] += num
        
        dp = {}
        def find(start):
            while start not in weights:
                start += 1
                if start > 10000:
                    return 0
            if start in dp:
                return dp[start]
            else:
                result = max(find(start+1), find(start+2) + weights[start])
                dp[start] = result
                return result
        return find(1)
    