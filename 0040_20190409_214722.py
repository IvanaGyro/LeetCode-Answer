class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.candidates = candidates
        self.ans = []
        self.dfs(target, 0, [])
        return self.ans
    
    def dfs(self, target, idx, path):
        last = None
        for i in range(idx, len(self.candidates)):
            num = self.candidates[i]
            if num == last:
                continue
            else:
                last = num
            if num > target:
                return
            if num == target:
                self.ans.append(path + [num])
                return
            self.dfs(target-num, i+1, path+[num])
