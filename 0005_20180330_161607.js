/**
 * @param {string} s
 * @return {string}
 */
var Node = function (l, r) {
    this.l = l;
    this.r = r;
    this.len = r - l + 1;
}


var findLP = function (s, l, r) {
    if (dp[l][r]) {
        return dp[l][r];
    }
    if (l == r) {
        dp[l][r] = new Node(l, r);
        return dp[l][r];
    }
    
    if (s.charAt(l) == s.charAt(r)) {
        if (r - l == 1) {
            dp[l][r] = new Node(l, r);
            return dp[l][r];
        }
        if (findLP(s, l+1, r-1).len == r-l-1) {
            dp[l][r] = new Node(l, r);
            return dp[l][r];
        }
    }
    var child1 = findLP(s, l, r-1);
    var child2 = findLP(s, l+1, r);
    dp[l][r] = child1.len < child2.len ? child2 : child1;
    return dp[l][r];   
}

var longestPalindrome = function(s) {
    dp = [];
    for(var i = 0; i < s.length; ++i) {
        dp[i] = [];
    }
    
    var ret = findLP(s, 0, s.length-1);
    return s.substr(ret.l, ret.len);
    
};