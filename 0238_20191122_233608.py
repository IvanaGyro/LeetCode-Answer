class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        num_len = len(nums)
        left = nums
        right = [1]*num_len
        for i in range(num_len-1):
            right[~i-1] = right[~i] * nums[~i]
        for i in range(num_len-1):
            left[i+1] *= left[i]
            right[i+1] *= left[i]
        return right