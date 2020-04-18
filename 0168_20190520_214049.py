class Solution:
    def convertToTitle(self, n: int) -> str:
        if n <= 0:
            return ''
        ans = ''
        while n:
            n -= 1
            n, r = divmod(n, 26)
            ans += chr(ord('A') + r)
        return ans[::-1]
        