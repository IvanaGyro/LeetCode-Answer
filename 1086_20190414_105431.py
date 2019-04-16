class Solution:
    tb = [None]*1001
    def divisorGame(self, N: int) -> bool:
        
        def dp(N):
            tb = Solution.tb
            if tb[N] is not None:
                return tb[N]
            
            win = False
            for i in range(1, (N >> 1) + 1):
                if N % i == 0:
                    if not dp(N-i):
                        win = True
                        break
            tb[N] = win
            return tb[N]
        return dp(N)
                
    
                
            
            
            