class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        counter = Counter(nums2)
        res = []
        for n in nums1:
            if counter[n] > 0:
                counter[n] -= 1
                res.append(n)
        return res