/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    var dp = Array.prototype.fill(false, 0, p.length);
    dp[0] = true;
    for (var i = 0; i < p.length; ++i) {
        dp[i+1] = i>0 && p.charAt(i) == '*' && dp[i-1]; 
    }
    
    for (var i = 0; i < s.length; ++i) {
        var last, cur;
        // dp[0] = s[0..i] matches ''
        // dp[j+1] = s[0..i] matches p[0..j]
        last = dp[0];
        dp[0] = false;
        for (var j = 0; j < p.length; ++j) {
            cur = dp[j+1];
            if (p.charAt(j) != '*') {
                dp[j+1] = last && (p.charAt(j) == '.' || s.charAt(i) == p.charAt(j)); 
            } else {
                dp[j+1] = dp[j-1] || dp[j+1] && (p.charAt(j-1) == '.' || s.charAt(i) == p.charAt(j-1))
            }
            last = cur;
        }
    }
    return dp[p.length];
};