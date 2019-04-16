class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict, Counter
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        table = defaultdict(list)
        for s in strs:
            counter = Counter(s)
            key = tuple(counter[c] for c in alphabets)
            table[key].append(s)
        return [v for k, v in table.items()]
        