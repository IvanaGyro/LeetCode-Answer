class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        pass
        if k <= 0:
            return False
        if t < 0:
            return False
        n = len(nums)
        k = min(k+1, n)
        min_num = min(nums)
        bucket = {}
        for i in range(n):
            if i >= k:
                key = (nums[i - k] - min_num) // (t + 1)
                del bucket[key]
            key = (nums[i] - min_num) // (t + 1)
            if key in bucket:
                return True
            for off in (-1, 1):
                if key + off in bucket and abs(bucket[key+off] - nums[i]) <= t:
                    return True
            bucket[key] = nums[i]
        return False