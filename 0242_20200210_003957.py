from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t: return True
        if len(s) != len(t): return False
        if not len(s): return False
        cnt = Counter(s)
        for c in t:
            if c not in cnt:
                return False
            cnt[c] -= 1
        for n in cnt.values():
            if n: return False
        return True