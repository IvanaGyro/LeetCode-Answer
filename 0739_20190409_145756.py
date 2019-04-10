class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        table = [None]*101
        for i in range(0, len(table)):
            table[i] = []
        for i, t in enumerate(T):
            for j in range(0, t+1):
                table[j].append(i)
            
        result = [None]*len(T)
        
        for i, t in enumerate(T):
            if t == 100:
                result[i] = 0
            else:
                day = 0
                for j in table[t+1]:
                    if j > i:
                        day = j - i
                        break
                result[i] = day
        return result