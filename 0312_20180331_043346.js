/**
 * @param {number[]} nums
 * @return {number}
 */
var dp = [];

var findMax = function(nums, l, r) {
    if (l > r) return 0;
    if (dp[l] === undefined) dp[l] = [];
    if (dp[l][r]) return dp[l][r];
    if (l == r) {
        dp[l][r] = nums[l-1]*nums[l]*nums[l+1];
        return dp[l][r];
    }
    
    var max = 0;
    for(var i = l; i <= r; ++i) {
        var coin = findMax(nums, l, i-1) + nums[l-1]*nums[i]*nums[r+1] + findMax(nums, i+1, r);
        max = Math.max(max, coin);
    }
    dp[l][r] = max;
    return max;
};

var maxCoins = function(nums) {
    dp = [];
    
    nums.unshift(1);
    nums.push(1);
    
    return findMax(nums, 1, nums.length-2);
};

