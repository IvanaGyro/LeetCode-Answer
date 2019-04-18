class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        prev = self.grayCode(n - 1)
        return prev + [(1 << n - 1) | prev[~i] for i in range(len(prev))]