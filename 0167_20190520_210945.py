from bisect import bisect_left
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            t = target - numbers[i]
            j = bisect_left(numbers, t, i + 1)
            if j < len(numbers) and numbers[j] == t:
                return [i + 1, j + 1]
            