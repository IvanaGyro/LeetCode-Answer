class Solution:
    def __init__(self):
        self.dp = {}
        
    def partition(self, s: str) -> List[List[str]]:
        def helper(s, l, r):
            if r - l == 0:
                return [[]]
            if r - l == 1:
                return [[s[l:r]]]
            res = []
            for i in range(r - 1, l - 1, -1):
                if self.isPalindrome(s, i, r):
                    res += [parts + [s[i:r]] for parts in helper(s, l, i)]
            return res
        return helper(s, 0, len(s))
    
    def isPalindrome(self, s, l, r):
        if (l, r) in self.dp:
            return self.dp[(l, r)]
        if l == r or l + 1 == r:
            return True
        self.dp[(l, r)] = self.isPalindrome(s, l + 1, r - 1) and s[l] == s[r - 1]
        return self.dp[(l, r)]