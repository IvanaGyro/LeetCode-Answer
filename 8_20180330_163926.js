/**
 * @param {string} str
 * @return {number}
 */
var myAtoi = function(str) {
    str = str.trim();
    var sign = 1;
    var num = 0;
    if (str.length < 1) return 0;
    if (str[0] == '+') {
        str = str.substr(1);
    } else if (str[0] == '-') {
        sign = -1;
        str = str.substr(1);
    }
    for (var i = 0; i < str.length; ++i) {
        if (str[i] >= '0' && str[i] <= '9') {
            num = num * 10 + str.charCodeAt(i) - 48; //'0'
        } else {
            break;
        }
    }
    num *= sign;
    num = num > 2147483647 ? 2147483647 : num;
    num = num < -2147483648 ? -2147483648 : num;
    return num;
};