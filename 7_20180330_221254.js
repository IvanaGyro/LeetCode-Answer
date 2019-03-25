/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    const MAX = 2147483647;
    const MIN = -2147483648;
    
    var sign = x < 0 ? -1 : 1;
    x = Math.abs(x).toString();
    x = parseInt(x.split('').reverse().join('')) * sign;
    if (x > MAX || x < MIN)
        return 0;
    return x;
    
};