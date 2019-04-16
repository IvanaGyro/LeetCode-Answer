class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        tb = [0]*len(s)
        
        for i in range(len(s)):
            if s[~i] == '0':
                tb[~i] = 0
                continue
            if ~i == -1:
                tb[~i] = 1
                continue
            if ~i == -2:
                tb[~i] = (int(s[~i:]) <= 26) + (s[~i+1] != '0')
                continue
            tb[~i] = tb[~i+1] + (int(s[~i:~i+2]) <= 26) * tb[~i+2]
            if tb[~i] == 0 and tb[~i+1] == 0:
                return 0
        
        return tb[0]
