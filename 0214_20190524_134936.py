class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        max_p = 0
        n = len(s)
        for i in range((n-1)>>1, -1, -1):
            if 2*i+2 <= n:
                if s[:2*i+2] == s[2*i+1::-1]:
                    max_p = 2*i+2
                    break
            if s[:2*i+1] == s[2*i::-1]:
                max_p = 2*i+1
                break
        return s[:max_p-1:-1] + s
    