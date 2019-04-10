class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        cnt = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                cnt += 1
            else:
                break
        return cnt
    