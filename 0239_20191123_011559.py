from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k <= 1:
            return nums
        n = len(nums)
        d = deque()
        result = [0]*(n-k+1)
        for i in range(n):
            while d and d[0] < i-k+1:
                d.popleft()
            while d and nums[d[-1]] <= nums[i]:
                d.pop()
            d.append(i)
            if i < k-1:
                continue
            result[i-k+1] = nums[d[0]]
        return result