class Solution:
    def customSortString(self, S: str, T: str) -> str:
        d = {}
        for i in range(len(S)):
            d[S[i]] = i
        T = ''.join(sorted(T, key=lambda x: d[x] if x in d else len(S) + ord(x) - ord('a')))
        return T