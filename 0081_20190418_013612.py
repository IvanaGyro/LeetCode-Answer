class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] == target:
                return True
            if nums[l] <= target < nums[mid]:
                r = mid
            elif nums[mid] < target <= nums[r - 1]:
                l = mid + 1
            elif nums[l] < nums[mid]:
                r = mid
            elif nums[mid] < nums[r - 1]:
                l = mid + 1
            else:
                return False
        return nums[l] == target