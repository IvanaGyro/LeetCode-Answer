class Solution:
    def combinationSum3(self, k: int, n: int, start: int = 1) -> List[List[int]]:
        if n > k * 9 or n < k * start:
            return []
        if k == 1:
            return [[n]]
        return [[i] + res for i in range(start, 10) for res in self.combinationSum3(k-1, n-i, i+1) ]
    