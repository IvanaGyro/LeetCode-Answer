class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if not t:
            return 1
        
        d = {}
        def helper(s, start, t):
            if (start, t) in d:
                return d[(start, t)]
            if len(s) - start < len(t):
                return 0
            if len(t) == 1:
                cnt = 0
                for i in range(len(s) - 1, start - 1, -1):
                    if s[i] == t:
                        cnt += 1
                    d[(i, t)] = cnt
            else:
                d[(start, t)] = 0
                if s[start] == t[0]:
                    d[(start, t)] += helper(s, start + 1, t[1:])
                d[(start, t)] += helper(s, start + 1, t)
            return d[(start, t)]
        
        return helper(s, 0, t)