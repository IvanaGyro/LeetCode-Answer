/**
 * @param {number[][]} matrix
 */
var NumMatrix = function(matrix) {
    this.table = [];
    matrix.forEach((row)=>{
        let map = [];
        map[0] = row;
        for (let n = 1; n < row.length; ++n) {
            map[n] = [];
            for (let i = 0; i < map[n-1].length-1; ++i) {
                map[n].push(map[n-1][i]+row[i+n]);
            }
        }
        this.table.push(map);
    });
};

/** 
 * @param {number} row1 
 * @param {number} col1 
 * @param {number} row2 
 * @param {number} col2
 * @return {number}
 */
NumMatrix.prototype.sumRegion = function(row1, col1, row2, col2) {
    var sum = 0,
        rlen = col2 - col1; // col2 - col1 + 1 -1, -1 to match the idx
    for (let i = row1; i <= row2; ++i) {
        sum += this.table[i][rlen][col1];
    }
    return sum;
};

/** 
 * Your NumMatrix object will be instantiated and called as such:
 * var obj = new NumMatrix(matrix)
 * var param_1 = obj.sumRegion(row1,col1,row2,col2)
 */