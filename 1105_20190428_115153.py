class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        if not A or not B:
            return 0
        if len(A) > len(B):
            A, B = B, A
        tb = [{} for _ in range(len(A))]
        for i in range(len(A) - 2, -1, -1):
            tb[i] = tb[i + 1].copy()
            tb[i][A[i + 1]] = i + 1
            
        dp = [[0]*len(B) for _ in range(len(A))]
        def connect(i, j):
            if i == len(A) or j == len(B):
                return 0
            if not dp[i][j]:
                if A[i] == B[j]:
                    dp[i][j] = max(dp[i][j], connect(i + 1, j + 1) + 1)
                elif B[j] not in tb[i]:
                    dp[i][j] = connect(i, j + 1)
                else:
                    dp[i][j] = max(connect(i, j + 1), connect(tb[i][B[j]], j))
            return dp[i][j]
        
        return connect(0, 0)
    
    