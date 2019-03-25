/**
 * @param {string} A
 * @param {string} B
 * @return {number}
 */
var repeatedStringMatch = function(A, B) {
    var offset = B.indexOf(A);
    if (offset >= A.length) return -1;
    if (offset == -1) { // not found
        if (B.length > A.length * 2 - 2) return -1;
        let len = A.length;
        A = A + A;
        offset = A.indexOf(B);
        if (offset == -1) return -1;
        if (offset + B.length <= len) return 1;
        if (offset >= len) return 1;
        return 2;
    } 

    var table = A.split('');
    var len = table.length;
    var ans = 0, key;
    for (let i = 0; i < B.length; ++i) {
        key = (i - offset + len) % len;
        if (table[key] != B[i]) return -1;
        if (key == len - 1) ++ans;
    }
    if (key != len - 1) ++ans;
    
    return ans;
};