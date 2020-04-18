class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        nums.append(nums[-1])
        res = []
        beg = end = nums[0]
        for n in nums[1:]:
            if n == end + 1:
                end += 1
            else:
                if end == beg:
                    res.append(str(beg))
                else:
                    res.append(f'{beg}->{end}')
                beg = end = n
        return res
    