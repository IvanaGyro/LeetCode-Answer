class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int: 
        n = len(customers)
        if n == 0:
            return 0
        bad = [customers[i] if grumpy[i] else 0 for i in range(n)]
        max_bad = wnd_bad = sum(bad[:X])
        for i in range(X, n):
            wnd_bad -= bad[i-X]
            wnd_bad += bad[i]
            max_bad = max(wnd_bad, max_bad)
        return sum(customers) - sum(bad) + max_bad
            