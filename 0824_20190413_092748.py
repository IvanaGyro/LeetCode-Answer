class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        length = 0
        line = 0
        for c in S:
            w = widths[ord(c) - ord('a')]
            if length + w > 100:
                line += 1
                length = 0
            length += w
        if length:
            line += 1
        return [line, length]
        