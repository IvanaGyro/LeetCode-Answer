class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        w = len(matrix[0])
        h = len(matrix)
        x = 0
        y = 0
        ans = []
        while w > 0 and h > 0:
            ans += matrix[y][x: x + w]
            ans += [matrix[j][x + w - 1] for j in range(y + 1, y + h)]
            if w >= 2 and h >= 2:
                ans += matrix[y + h -1][x + w - 2: x - 1 if x else None: -1]
                ans += [matrix[j][x] for j in range(y + h - 2, y, -1)]
            w -= 2
            h -= 2
            x += 1
            y += 1
        return ans