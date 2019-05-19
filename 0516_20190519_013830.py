class Solution:
    def longestPalindromeSubseq(self, s):
        dp = [[0]*len(s) for _ in range(len(s))]
        max_ = 0
        for i in range(len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i - 1][j + 1] + 2 if i > 0 and j < len(s) - 1 else 2
                else:
                    dp[i][j] = max(
                        dp[i - 1][j] if i > 0 else 0,
                        dp[i][j + 1] if j < len(s) - 1 else 0,
                    )
                if j - i <= 1:
                    if i == j:
                        dp[i][j] -= 1
                    max_ = max(max_, dp[i][j])

        return max_ +1