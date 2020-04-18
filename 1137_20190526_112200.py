class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        order = sorted(heights)
        return sum(order[i] != heights[i] for i in range(len(heights)))
    