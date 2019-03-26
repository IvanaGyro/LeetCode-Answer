/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if (nums.lenght == 0) return 0;
    var max_arr = new Array(nums.length);
    max_arr.fill(null);
    var helper = function(idx) {
        if (idx >= max_arr.length) return 0;
        if (max_arr[idx] !== null) return max_arr[idx];
        max_arr[idx] = Math.max(helper(idx+1), helper(idx+2) + nums[idx]);
        return max_arr[idx];
    }
    return helper(0);
};