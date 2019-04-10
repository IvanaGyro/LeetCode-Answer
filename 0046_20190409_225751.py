class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        self.nums = nums
        self.res = []
        self.dfs([False]*len(nums), [])
        return self.res
    
    def dfs(self, mask, path):
        for i in range(len(self.nums)):
            if mask[i]:
                continue
            if len(path) == len(self.nums)-1:
                self.res.append(path + [self.nums[i]])
            else:
                mask[i] = True
                self.dfs(mask, path + [self.nums[i]])
                mask[i] = False