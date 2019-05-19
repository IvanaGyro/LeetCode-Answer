class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one, two = 0, 0
        for n in nums:
            one = (one ^ n) & ~two
            two = (two ^ n) & ~one
        return one