from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = Counter()
        for n in nums:
            cnt[n] += 1
            if len(cnt) == 3:
                cnt -= Counter(cnt.keys())
        cnt = Counter(n for n in nums if n in cnt)
        return [n for n in cnt if cnt[n] > len(nums) // 3]
    