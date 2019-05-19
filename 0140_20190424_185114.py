class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s:
            return []
        
        from collections import defaultdict
        d = defaultdict(lambda: defaultdict(list))
        alpha = [False]*26
        
        for w in wordDict:
            d[w[0]][len(w)].append(w)

        tb = [None]*(len(s)+1)
        tb[-1] = ['']
        
        def dp(b):
            nonlocal s
            if tb[b] is not None:
                return tb[b]

            tb[b] = []
            for l in d[s[b]]:
                if s[b:b+l] in d[s[b]][l]:
                    tb[b] += [s[b:b+l] + (ss and " " + ss) for ss in dp(b+l)]
            return tb[b]
        
        return dp(0)

