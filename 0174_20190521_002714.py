from math import inf
from collections import defaultdict
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon or not dungeon[0]:
            return 0
        h, w = len(dungeon), len(dungeon[0])
        hp = [inf] * (w + 1)
        hp[-2] = 1

        for i in range(h - 1, -1, -1):
            for j in range(w - 1, -1, -1):
                hp[j] = min(hp[j], hp[j + 1]) - dungeon[i][j]
                hp[j] = hp[j] if hp[j] > 0 else 1
        return hp[0]
    