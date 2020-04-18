class Solution:
    def titleToNumber(self, s: str) -> int:
        return self.titleToNumber(s[:-1]) * 26 + ord(s[-1]) - ord('A') + 1 if s else 0
    