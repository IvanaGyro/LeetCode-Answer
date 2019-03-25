/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    var arr = s.split('');
    var subArr = [], subDict = [];
    var r = 0, len = 0;
    while (r < arr.length) {
        while (subDict[arr[r]]) {
            var first = subArr.shift();
            subDict[first] = null;
        }
        subArr.push(arr[r]);
        subDict[arr[r]] = true;
        len = subArr.length > len ? subArr.length : len;
        r++;
    }
    return len;
};