class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0 or n == 0:
            return []
        ans = []
        def dfs(cur, path):
            nonlocal n, k
            for i in range(cur, n + len(path) - k + 2):
                path.append(i)
                if len(path) == k:
                    ans.append(path[:])
                else:
                    dfs(i + 1, path)
                path.pop()
        
        dfs(1, [])
        return ans
                
            