class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ch_map = {}
        matched = set()
        for i in range(len(s)):
            if s[i] not in ch_map:
                if t[i] in matched:
                    return False
                ch_map[s[i]] = t[i]
                matched.add(t[i])
            elif ch_map[s[i]] != t[i]:
                return False
        return True
                