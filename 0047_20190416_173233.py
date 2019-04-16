class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        self.nums = nums
        self.ans = []
        self.permute(0)
        return self.ans
        
    def permute(self, cur):
        if cur == len(self.nums) - 1:
            self.ans.append(self.nums[:])
            return
        self.permute(cur+1)
        for i in range(cur+1, len(self.nums)):
            if self.nums[cur] != self.nums[i]:
                self.nums[cur], self.nums[i] = self.nums[i], self.nums[cur]
                self.permute(cur+1)
            
        for i in range(cur, len(self.nums)-1):
            if self.nums[i] == self.nums[i+1]:
                continue
            self.nums[i], self.nums[i+1] = self.nums[i+1], self.nums[i]
        
            