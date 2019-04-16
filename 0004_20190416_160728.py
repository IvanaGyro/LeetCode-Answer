class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            if not nums1:
                nums1 = [nums2[0], nums2[-1]]
            return self.find(nums1, 0, len(nums1), nums2, 0, len(nums2))
        else:
            if not nums2:
                nums2 = [nums1[0], nums1[-1]]
            return self.find(nums2, 0, len(nums2), nums1, 0, len(nums1))
                
    
    def find(self, short, s_l_b, s_r_b, long, l_l_b, l_r_b):
        # print(short, s_l_b, s_r_b, long, l_l_b, l_r_b)
        if s_r_b - s_l_b == 1:
            if l_r_b - l_l_b == 1:
                return (short[s_l_b] + long[l_l_b]) / 2
            else:
                s = short[s_l_b]
                l_l_idx, l_l, l_r_idx, l_r = self.getBound(long, l_l_b, l_r_b)
                if s > l_r:
                    if not self.isAdjacent(long, (l_r_idx, l_r), short, (s_l_b, s)):
                        if (l_r_b - l_l_b) & 1:
                            return (l_r + long[l_r_idx]) / 2
                        else:
                            return l_r
                elif s < l_l:
                    if not self.isAdjacent(short, (s_r_b, s), long, (l_l_idx, l_l)):
                        if (l_r_b - l_l_b) & 1:
                            return (l_l + long[l_l_idx-1]) / 2
                        else:
                            return l_l
                else:
                    return s

            
        s_l_idx, s_l, s_r_idx, s_r = self.getBound(short, s_l_b, s_r_b)
        l_l_idx, l_l, l_r_idx, l_r = self.getBound(long, l_l_b, l_r_b)
        
            
        if s_l > l_r:
            if not self.isAdjacent(long, (l_r_idx, l_r), short, (s_l_idx, s_l)):
                return self.find(short, s_l_b, s_l_idx + 1, long, l_l_b + (s_r_b - s_l_idx - 1), l_r_b)
                        
        elif s_r < l_l:
            if not self.isAdjacent(short, (s_r_idx, s_r), long, (l_l_idx, l_l)):
                return self.find(short, s_r_idx - 1, s_r_b, long, l_l_b, l_r_b - (s_r_idx - s_l_b - 1))
        tmp = []
        if s_r_idx - s_l_idx == 1:
            tmp += [s_l]
        else:
            tmp += [s_l, s_r]
        if l_r_idx - l_l_idx == 1:
            tmp += [l_l]
        else:
            tmp += [l_l, l_r]
        tmp.sort()
        # # print(tmp)
        if len(tmp) & 1:
            return tmp[1]
        else:
            mid = len(tmp) >> 1
            return (tmp[mid-1] + tmp[mid]) / 2            
        
    def getBound(self, nums, l, r):
        mid = l + r >> 1
        if (r - l) & 1:
            return mid, nums[mid], mid + 1, nums[mid]
        else:
            return mid-1, nums[mid-1], mid + 1, nums[mid]
        
    def isAdjacent(self, n1, b1, n2, b2):
        # print(n1, b1, n2, b2)
        # b1 < b2
        r1, rv1 = b1
        l2, lv2 = b2
        
        if r1 < len(n1) or l2 > 0:
            if r1 < len(n1) and n1[r1] <= lv2:
                return False
            if l2 > 0 and n2[l2-1] >= rv1:
                return False
        return True
        
    def _findMedianSortedArrays(self, nums1, nums2):
        tasks = [
            ([1, 3], [2], 2),
            ([3], [1, 2], 2),
            ([1, 2], [3, 4], 2.5),
            ([1, 2, 3, 4], [5], 3),
            ([1, 2, 3], [5], 2.5),
            ([1, 2, 5, 6], [3, 4], 3.5),
            ([1, 2, 4, 6], [3, 5], 3.5),
            ([1, 2, 7, 8], [3, 4, 5], 4),
            ([1, 7, 8, 9], [3, 4, 5], 5),
            ([1, 2, 3, 4], [5, 6], 3.5),
            ([1, 1, 2], [2], 1.5),
            ([1, 1, 1, 2], [2, 2], 1.5),
            ([100001], [100000], 100000.5),
            ([100000], [100001], 100000.5),
            ([2], [1,3,4], 2.5),
            ([3], [-2,-1], -1.0),
            ([1], [2,3,4], 2.5),
            ([1,2,5], [3,4,6], 3.5),
            ([], [1],1),
        ]
        
        for nums1, nums2, ans in tasks:
            res = self._findMedianSortedArrays(nums1, nums2)
            if res != ans:
                print(nums1, nums2, res)
        