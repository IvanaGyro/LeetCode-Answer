class Solution:
    def countPrimes(self, n: int) -> int:
        nums = [None] * n
        cnt = 0
        for i in range(2, n):
            if nums[i] is None:
                nums[i] = True
                cnt += 1
                j = i << 1
                while j < n:
                    nums[j] = False
                    j += i
        return cnt
    