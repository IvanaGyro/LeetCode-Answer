class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        if not grid or not grid[0]:
            return grid
        prev = grid[r0][c0]
        if prev == color:
            return grid
        
        visited = [[None]*len(grid[0]) for _ in range(len(grid))]
        
        def flood(r, c):
            if grid[r][c] != prev or visited[r][c]:
                return
            visited[r][c] = True
            nexts = [(nr, nc)
                     for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)] 
                     if 0 <= nr < len(grid) and 0 <= nc < len(grid[0])]
            is_border = len(nexts) < 4 or any(grid[x][y] != prev for x, y in nexts)
            for x, y in nexts:
                flood(x, y)
            if is_border:
                grid[r][c] = color
        
        flood(r0, c0)
        return grid
