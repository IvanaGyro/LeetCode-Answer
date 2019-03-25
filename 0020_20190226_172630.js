/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    var stack = [];
    var table = {
        ')':'(',
        ']':'[',
        '}':'{'
    }
    for (let c of s) {
        if (c == '(' || c == '[' || c == '{') stack.push(c);
        else{
            const c_ = stack.pop();
            
            if (table[c] != c_ || table[c] === undefined) return false;
        }
    }
    return stack.length == 0
};