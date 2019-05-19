#include <algorithm>

using namespace std;

class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        if(!grid.size() || !grid[0].size()) return 0;
        p_grid = &grid;
        m = grid.size(), n = grid[0].size();
        
        visited = vector<vector<bool>>(m);
        for(auto&& v : visited) {
            v = vector<bool>(n, false);
        }
        
        size_t max_area = 0;
        for(int x = 0; x < m; ++x) {
            for(int y = 0; y < n; ++y) {
                if (grid[x][y] && !visited[x][y]) {
                    max_area = max(max_area, get_area(x, y));
                }
            }
        }
        return max_area;
    }

private:
    vector<vector<int>> *p_grid;
    vector<vector<bool>> visited;
    size_t area, m, n;
    
    size_t get_area(size_t x, size_t y) {
        area = 0;
        flood(x, y);
        return area;
    }
    
    void flood(size_t x, size_t y) {
        if (x < 0 || x >= m || y < 0 || y >= n) return;
        if (visited[x][y] || !(*p_grid)[x][y]) return;
        visited[x][y] = true;
        ++area;
        flood(x - 1, y);
        flood(x + 1, y);
        flood(x, y - 1);
        flood(x, y + 1);
    }
    
};