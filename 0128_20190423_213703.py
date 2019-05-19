class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxCnt = 0
        while s:
            n = m = s.pop()
            cnt = 1
            while m - 1 in s:
                s.remove(m - 1)
                m -= 1
                cnt += 1
            while n + 1 in s:
                s.remove(n + 1)
                n += 1
                cnt += 1
            maxCnt = max(maxCnt, cnt)
        return maxCnt