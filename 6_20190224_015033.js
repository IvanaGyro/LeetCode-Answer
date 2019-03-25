/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    if (numRows === 1) return s;
    const length = s.length
    var jump = numRows * 2 - 2;
    var result = '';
    var curLength = 0;
    for (let i = 0; i < numRows; ++i) {
        let j = i;
        if (i === 0 || i === numRows - 1) {
            while (j < length) {
                result += s[j];
                j += jump;
            }
        } else {
            const subJumps = [jump - i * 2, i * 2];
            let state = 0;
            while (j < length) {
                result += s[j];
                j += subJumps[state];
                state ^= 1;
            }
        }
    }
    return result;
};
/*
1     7    3   6 0 6 0 6 0 
2   6 8  2 4   4 2 4 2 4 2
3 5   9 1      2 4 2 4 2 4
4     0        0 6 0 6 0 6 

1   5   9   3  4 0 4 0 4 0
2 4 6 8 0 2 4  2 2 2 2 2 2 
3   7   1      0 4 0 4 0 4

1       9       7    8 0 8 0 8 0   mod 2r-2 === 0
2     8 0     6 8    6 2 6 2 6 2   
3   7   1   5   9    4 4 4 4 4 4 
4 6     2 4     0    2 6 2 6 2 6
5       3       1    0 8 0 8 0 8  mod 2r-2 === r-1
*/