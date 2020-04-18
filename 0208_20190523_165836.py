from collections import defaultdict
class Trie:

    def __init__(self):
        self.word_map = defaultdict(set)
        

    def insert(self, word: str) -> None:
        for i in range(len(word)):
            self.word_map[word[:i+1]].add(word)
        

    def search(self, word: str) -> bool:
        return word in self.word_map[word]
        

    def startsWith(self, prefix: str) -> bool:
        return bool(self.word_map[prefix])
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)