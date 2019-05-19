class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diffs = sorted(costs, key=lambda x: x[0] - x[1])
        mid = len(diffs)>>1
        ans = sum([A for A, B in diffs[:mid]])
        ans += sum([B for A, B in diffs[mid:]])
        return ans
    