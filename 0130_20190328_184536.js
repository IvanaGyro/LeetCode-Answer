/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solve = function(board) {
    if (board.length == 0) return board;
    var freez = new Array(board.length).fill(0);
    freez.forEach((_, i, arr)=>{
        arr[i] = new Array(board[0].length).fill(0);
    });
    var helper = function(x, y, is_border) {
        var target,
            after;
        if (is_border) {
            target = freez;
            after = 1;
        } else {
            target = board;
            after = 'X';
        }
        
        var flood = function(x, y) {
            if (board[x][y] == 'X' || freez[x][y] == 1) return;
            target[x][y] = after;
            if (x-1 >= 0) flood(x-1, y);
            if (x+1 < board.length) flood(x+1, y);
            if (y-1 >= 0) flood(x, y-1);
            if (y+1 < board[0].length) flood(x, y+1);
        };
        flood(x, y);
    };
    for (let i = 0; i < board.length; ++i) {
        if (board[i][0] == 'O' & freez[i][0] == 0) helper(i, 0, true);
        if (board[i][board[i].length-1] == 'O' & freez[i][board[i].length-1] == 0) helper(i, board[i].length-1, true);
    }
    for (let j = 1; j < board[0].length-1; ++j) {
        if (board[0][j] == 'O' & freez[0][j] == 0) helper(0, j, true);
        if (board[board.length-1][j] == 'O' & freez[board.length-1][j] == 0) helper(board.length-1, j, true);
    }
    for (let i = 1; i < board.length-1; ++i) {
        for (let j = 1; j < board[0].length-1; ++j) {
            if (board[i][j] == 'O' & freez[i][j] == 0) helper(i, j, false);
        }
    }
    return board;
};