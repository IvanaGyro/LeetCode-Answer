from collections import defaultdict
class WordDictionary:

    def __init__(self):
        T = lambda: defaultdict(T)
        self.wordDict = defaultdict(T)
        

    def addWord(self, word: str) -> None:
        n = self.wordDict
        for c in word:
            n = n[c]
        n['#']
        

    def search(self, word: str) -> bool:
        nodes = [self.wordDict]
        for c in word:
            if c == '.':
                nodes = [n for node in nodes for n in node.values()]
            else:
                nodes = [node[c] for node in nodes if c in node]
        return any('#' in node for node in nodes)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)