/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
    const MAX = 2147483647;
    var ans = dividend / divisor;
    if (ans < 0) return Math.ceil(ans);
    ans = Math.floor(ans);
    if (ans > MAX) return MAX;
    return ans;
};