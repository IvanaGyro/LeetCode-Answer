from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        visited = defaultdict(int)
        res = []
        for i in range(len(s)-9):
            dna = s[i:i+10]
            if visited[dna] == 1:
                res.append(dna)
            visited[dna] += 1
        return res
    