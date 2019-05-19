from collections import Counter
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        cnt = Counter(candies)
        if len(cnt) >= len(candies) // 2:
            return len(candies) // 2
        else:
            return len(cnt)
        