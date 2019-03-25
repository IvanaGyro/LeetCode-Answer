/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if (strs.length == 0) return '';
    if (strs.length == 1) return strs[0];
    
    var minLen = strs[0].length;
    for (let i = 1; i < strs.length; ++i) {
        minLen = strs[i].length < minLen ? strs[i].length : minLen;
    }
    
    var result = '';
    for (let i = 0; i < minLen; ++i) {
        let c = strs[0][i];
        for (let j = 1; j < strs.length; ++j) {
            if (strs[j][i] != c) return result;
        }
        result += c;
    }
    return result;
};