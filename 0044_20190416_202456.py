class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sp = pp = 0
        while sp < len(s) and pp < len(p):
            if p[pp] == '*':
                while p[pp] == '*':
                    pp += 1
                    if pp == len(p):
                        return True
                while sp < len(s):
                    if (s[sp] == p[pp] or p[pp] == '?') and self.isMatch(s[sp:], p[pp:]):
                        return True
                    sp += 1
                return False
            elif p[pp] == '?':
                pp += 1
                sp += 1
            else:
                if p[pp] != s[sp]:
                    return False
                pp += 1
                sp += 1
        while pp < len(p) and p[pp] == '*':
            pp += 1
        return sp == len(s) and pp == len(p)