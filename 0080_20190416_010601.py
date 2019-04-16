class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        def swap(arr, a, b):
            tmp = arr[a]
            arr[a] = arr[b]
            arr[b] = tmp
        prev = None
        l = 0
        cnt = 0
        for r in range(len(nums)):
            if nums[r] != prev:
                prev = nums[r]
                cnt = 0
            if cnt < 2:
                swap(nums, l, r)
                l += 1
                cnt += 1
        return l