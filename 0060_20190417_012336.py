class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if not hasattr(Solution, 'factorials'):
            self.init()
        chars = [str(n) for n in range(1, n + 1)]
        k -= 1
        ans = []
        for i in range(n-1, -1, -1):
            ans.append(chars.pop(k // self.factorials[i]))
            k %= self.factorials[i]
        return ''.join(ans)
    
    def init(self):
        Solution.factorials = [1]*10
        for i in range(1, 10):
            Solution.factorials[i] = Solution.factorials[i-1] * i