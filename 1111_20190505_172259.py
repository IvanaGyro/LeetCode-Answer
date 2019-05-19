from math import inf
class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        dp = [[None]*len(A) for _ in range(len(A))]
        
        def helper(i, j):
            if j - i == 1:
                return 0
            if dp[i][j] is None:
                dp[i][j] = min(helper(i, k) + helper(k, j) + A[i] * A[j] * A[k] for k in range(i + 1, j))
            return dp[i][j]

        return helper(0, len(A) - 1)
    