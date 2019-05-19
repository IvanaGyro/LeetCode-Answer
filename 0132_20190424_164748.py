class Solution:
    def minCut(self, s):
        from math import inf
        tb = [inf]*(len(s) + 1)
        tb[0] = -1
        for i in range(len(s)):
            odd_valid = True
            even_valid = True
            for j in range(len(s)):
                if odd_valid and i - j >= 0 and i + j < len(s) and s[i-j] == s[i + j]:
                    tb[i+j+1] = min(tb[i+j+1], tb[i-j] + 1)
                else:
                    odd_valid = False
                if even_valid and i-j-1 >= 0 and i + j < len(s) and s[i-j-1] == s[i+j]:
                    tb[i+j+1] = min(tb[i+j+1], tb[i-j-1] + 1)
                else:
                    even_valid = False
                if not odd_valid and not even_valid:
                    break
        return tb[len(s)]