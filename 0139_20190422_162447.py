class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not hasattr(self, 'wordDict'):
            self.init(wordDict)
        waiting = [self.wordDict]
        for c in s:
            waiting = [n[c] for n in waiting if c in n]
            if any(n['##'] for n in waiting):
                waiting += [self.wordDict]
        return any(n['##'] for n in waiting)
            
    
    def init(self, wordDict):
        from collections import defaultdict
        t = lambda: defaultdict(t)
        self.wordDict = defaultdict(t)
        for word in wordDict:
            cur = self.wordDict
            for c in word:
                cur = cur[c]
            cur['##'] = True
