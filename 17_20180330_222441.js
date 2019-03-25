/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    var tb = [
        [' '], [''], ['a', 'b', 'c'], ['d', 'e', 'f'],
        ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
        ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']
    ]
    var ret = [''];
    for (var i = 0; i < digits.length; ++i) {
        var newRet = [];
        for (var j = 0; j < ret.length; ++j) {
            for (var k = 0; k < tb[digits[i]].length; ++k) {
                newRet.push(ret[j] + tb[digits[i]][k]);
            }
        }
        ret = newRet;
    }
    if (ret.length == 1 && ret[0] == '') ret = [];
    return ret;
};