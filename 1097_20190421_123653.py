class StreamChecker:

    def __init__(self, words: List[str]):
        from collections import deque
        tmp = set(words)
        tmp = sorted(tmp, key=lambda word: -len(word))
        self.words = []
        self.queries = ''
        
        while len(tmp):
            word = tmp.pop()
            j = 0
            while j < len(tmp):
                if tmp[j][-len(word):] == word:
                    tmp.pop(j)
                else:
                    j += 1
            self.words.append(word)
            
        self.maxlen = len(self.words[-1]) if self.words else 0

    def query(self, letter: str) -> bool:
        self.queries = self.queries[-self.maxlen+1:] + letter
        for word in self.words:
            if self.queries.find(word, -len(word)) != -1:
                return True
        return False

        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)