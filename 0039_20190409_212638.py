class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def find(combination, target):
            for num in candidates:
                if combination and num < combination[-1]:
                    continue
                if num == target:
                    combination.append(num)
                    ans.append(combination.copy())
                    combination.pop()
                    return
                if num < target:
                    combination.append(num)
                    find(combination, target - num)
                    combination.pop()
                else:
                    return
        find([], target)
        return ans