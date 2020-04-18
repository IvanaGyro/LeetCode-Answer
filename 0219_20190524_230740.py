from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k <= 0:
            return False
        k = min(k + 1, len(nums))
        cnt = defaultdict(int)
        for i in range(k):
            num = nums[i]
            cnt[num] += 1
            if cnt[num] > 1:
                return True
        for i in range(k, len(nums)):
            cnt[nums[i-k]] -= 1
            num = nums[i]
            cnt[num] += 1
            if cnt[num] > 1:
                return True
        return False
    