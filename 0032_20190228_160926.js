/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function(s) {
    var stack = [], barriers = [-1], ans = 0;
    for (let i = 0; i < s.length; ++i) {
        if (s[i] == '(') {
            barriers.push(i);
            stack.push(1);
        } else {
            if (stack.length > 0) {
                barriers.pop();
                stack.pop();
            } else {
                barriers.push(i);
            }
        }
    }
    barriers.push(s.length);
    for (let i = 1; i < barriers.length; ++i) {
        let cnt = barriers[i] - barriers[i-1] - 1;
        ans = cnt > ans ? cnt : ans;
    }
    return ans;
};