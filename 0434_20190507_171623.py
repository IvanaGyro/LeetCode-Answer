class Solution:
    def countSegments(self, s: str) -> int:
        return len([_ for _ in s.split(' ') if _])