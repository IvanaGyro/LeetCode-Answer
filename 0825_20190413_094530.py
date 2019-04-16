class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        v_line = [0]*len(grid)
        h_line = [0]*len(grid) 
        for i in range(len(grid)):
            for j in range(len(grid)):
                v_line[j] = max(v_line[j], grid[i][j])
                h_line[i] = max(h_line[i], grid[i][j])
        
        sum = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                sum += min(v_line[j], h_line[i]) - grid[i][j]
                
        return sum