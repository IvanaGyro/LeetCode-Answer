class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        import bisect
        l, r = newInterval
        lidx = bisect.bisect(intervals, [l])
        if lidx > 0:
            if intervals[lidx-1][1] >= l:
                lidx -= 1
        ridx = bisect.bisect(intervals, [r])
        if ridx != len(intervals) and intervals[ridx][0] == r:
            ridx += 1
        
        if lidx != ridx:
            l = min(l, intervals[lidx][0])
            r = max(r, intervals[ridx-1][1])
        ans = intervals[:lidx]
        ans.append([l, r])
        ans += intervals[ridx:]
        return ans
        
        