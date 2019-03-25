/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    var ans = [];
    var arr = [];
    var addParenthesis = function(remain, arr, open) {
        if (remain > 0) {
            arr.push('(');
            addParenthesis(remain - 1, arr, open + 1);
            arr.pop();
        }
        if (open > 0) {
            arr.push(')');
            addParenthesis(remain, arr, open - 1);
            arr.pop();
        }
        if (remain == 0 && open == 0) ans.push(arr.join(''));
    }
    addParenthesis(n, arr, 0);
    return ans;
};