class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter(nums)
        for k, v in counter.items():
            if v == 1:
                return k
        assert False