class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        profit = 0
        min_p = prices[0]
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - min_p)
            min_p = min(min_p, prices[i])
        return profit