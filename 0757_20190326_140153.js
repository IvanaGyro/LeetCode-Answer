/**
 * @param {string} bottom
 * @param {string[]} allowed
 * @return {boolean}
 */
var transition = function(bottom, second, allowed, level) {
    if (level == 1) return true;
    for (var i = 0; i < 7; ++i) {
        if (allowed[bottom[0]][bottom[1]][i]) {
            second.push(i);
            let result;
            if (bottom.length == 2) {
                result = transition(second, [], allowed, level-1);
            } else {
                result = transition(bottom.slice(1), second, allowed, level);
            }
            
            if (result) return true;
            second.pop();
        }
    }
    return false;
};

function createArray(length) {
    var arr = new Array(length || 0),
        i = length;
    

    if (arguments.length > 1) {
        var args = Array.prototype.slice.call(arguments, 1);
        while(i--) arr[length-1 - i] = createArray.apply(this, args);
    } else {
        arr.fill(0);
    }

    return arr;
}

var str2arr = function(s) {
    var arr = s.split('');
    return arr.map((c)=>{return c.charCodeAt() - 65;});
}

var pyramidTransition = function(bottom, allowed) {
    var table = createArray(7, 7, 7);
    allowed.forEach((val)=>{table[val.charCodeAt(0)-65][val.charCodeAt(1)-65][val.charCodeAt(2)-65]++;});
    return transition(str2arr(bottom), [], table, bottom.length);
};