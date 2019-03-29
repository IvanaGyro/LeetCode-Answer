/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    var island = 0;
    var flood = function(x, y) {
        if (grid[x][y] == '0') return;
        grid[x][y] = '0';
        if (x-1 >= 0) flood(x-1, y);
        if (x+1 < grid.length) flood(x+1, y);
        if (y-1 >= 0) flood(x, y-1);
        if (y+1 < grid[x].length) flood(x, y+1);
    };
    for (let i = 0; i < grid.length; ++i) {
        for (let j = 0; j < grid[i].length; ++j) {
            if (grid[i][j] == '1') {
                ++island;
                flood(i, j);
            }
        }
    }
    return island;
};