class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        if stones[-1] - stones[0] == len(stones) - 1:
            min_ = 0
        elif stones[-2] - stones[0] == len(stones) - 1 or stones[-1] - stones[1] == len(stones) - 1:
            min_ = 1
        elif stones[-2] - stones[0] == len(stones) - 2 or stones[-1] - stones[1] == len(stones) - 2:
            min_ = 2
        else:
            l, r = 0, 0
            min_ = len(stones)
            for l in range(len(stones)):
                while r < len(stones) and stones[r] - stones[l] <= len(stones) - 1:
                    r += 1
                min_ = min(len(stones) - (r - l), min_)

        max_ = max(stones[-1] - stones[1], stones[-2] - stones[0]) - len(stones) + 2
        return [min_, max_]
        