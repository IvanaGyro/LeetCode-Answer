class Solution:
    def candy(self, ratings: List[int]) -> int:
        downhill_len, cur, sum = 0, 1, 1
        ratings.append(ratings[-1])
        for i in range(1, len(ratings)):
            if ratings[i] >= ratings[i-1]:
                if downhill_len:
                    if cur < 1:
                        downhill_len += 1
                    sum -= (cur - 1) * downhill_len
                    downhill_len = 0
                    cur = 1
                if ratings[i] > ratings[i-1]:
                    cur += 1
                else:
                    cur = 1
            else:
                cur -= 1
                downhill_len += 1
            sum += cur
        return sum-1
            
        
        
        
        
        candies = [1]*len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        return sum(candies)