class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        w = min(C, G) - max(A, E)
        h = min(D, H) - max(B, F)
        if w <= 0 or h <= 0:
            cover = 0
        else:
            cover = w * h
        return (C-A)*(D-B) + (G-E)*(H-F) - cover
    