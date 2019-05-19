from math import inf
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1, sold1, buy2, sold2 = -inf, 0, -inf, 0
        
        for p in prices:
            sold2 = max(sold2, buy2 + p)
            buy2 = max(buy2, sold1 - p)
            sold1 = max(sold1, buy1 + p)
            buy1 = max(buy1, -p)
        
        return sold2