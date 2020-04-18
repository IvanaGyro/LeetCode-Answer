from math import inf
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        n = len(prices)
        
        if k >= n >> 1:
            return sum(max(prices[i] - prices[i - 1], 0) for i in range(1, n))

        buys = [-prices[0]] * k
        sells = [0] * (k + 1)
        for price in prices:
            for i in range(k):
                sells[i] = max(sells[i], buys[i] + price)
                buys[i] = max(buys[i], sells[i + 1] - price)
        return sells[0]
    