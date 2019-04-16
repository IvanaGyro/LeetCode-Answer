class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m):
            nums1[~i] = nums1[~i - n]

        p1 = n
        p2 = 0
        for i in range(m + n):
            if p2 == n or p1 < m + n and nums1[p1] < nums2[p2]:
                nums1[i] = nums1[p1]
                p1 += 1
            else:
                nums1[i] = nums2[p2]
                p2 += 1
        