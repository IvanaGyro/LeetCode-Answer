class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        from collections import Counter
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        def to_morse(s):
            morses = [table[ord(c) - ord('a')] for c in s]
            return ''.join(morses)
        
        count = Counter([to_morse(word) for word in words])
        return len(count)