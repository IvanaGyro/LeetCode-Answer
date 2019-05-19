class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import defaultdict
        d = defaultdict(set)
        for w in wordList:
            for i in range(len(w)):
                d[w[:i] + '_' + w[i+1:]].add(w)

        q = set((beginWord,))
        cnt = 1
        while q:
            if endWord in q:
                return cnt
            cnt += 1
            nq = set()
            for s in q:
                for i in range(len(s)):
                    key = s[:i] + '_' + s[i + 1:]
                    nq |= d[key]
                    d[key].clear()
            q = nq
        return 0
                    