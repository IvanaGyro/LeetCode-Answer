from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return any(val >= 2 for val in Counter(nums).values())
    