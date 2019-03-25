/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    var table = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M':1000
    }
    var num = 0;
    for (var i = 0; i < s.length; ++i) {
        if (i < s.length - 1) {
            if (table[s[i]] >= table[s[i+1]]) {
                num += table[s[i]];
            } else {
                num += table[s[i+1]];
                num -= table[s[i]];
                ++i;
            }
        } else {
            num += table[s[i]];
        }
    }
    return num;
};