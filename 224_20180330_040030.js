/**
 * @param {string} s
 * @return {number}
 */
var calculate = function(s) {
    s = s.replace(/ /g, '');
    var opStack = [''], numStack = [];

    for (var i = 0; i < s.length; ++i) {
        var num = '';
        while (s.charAt(i) >= '0' && s.charAt(i) <= '9') {
            num += s.charAt(i);
            ++i;
        }
        if (num != '') {
            numStack.push(parseInt(num));
        }
        if (i < s.length) {
            if (s.charAt(i) == '(') {
                opStack.push('(');
            } else if (s.charAt(i) == ')') {
                var op;
                while ((op = opStack.pop()) != '(') {
                    if (op == '+') {
                        numStack.push(numStack.pop() + numStack.pop());
                    } else if (op == '-') {
                        numStack.push(-numStack.pop() + numStack.pop());
                    }
                }
            } else {
                var lastOp = opStack[opStack.length-1];
                if (lastOp == '+' || lastOp == '-') {
                    lastOp = opStack.pop();
                    if (lastOp == '+') {
                        numStack.push(numStack.pop() + numStack.pop());
                    } else if (lastOp == '-') {
                        numStack.push(-numStack.pop() + numStack.pop());
                    }
                }
                opStack.push(s.charAt(i));
            }
        }

    }
    var op;
    while ((op = opStack.pop()) != '') {
        if (op == '+') {
            numStack.push(numStack.pop() + numStack.pop());
        } else if (op == '-') {
            numStack.push(-numStack.pop() + numStack.pop());
        }
    }
    return numStack.pop();
};