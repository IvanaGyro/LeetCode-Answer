/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    if (!nums.length) return [-1, -1];
    
    var l = 0,
        r = nums.length - 1,
        c = l + r >> 1;
    while (nums[c] != target && l < r) {
        if (target < nums[c]) r = c - 1;
        else l = c + 1;
        c = l + r >> 1;
    }
    if (nums[c] != target) return [-1, -1];
    
    var l2 = l,
        r2 = c,
        c2 = l2 + r2 >> 1,
        ans = Array(2);
    while (nums[c2] != target || (c2 > l2 && nums[c2-1] == target)) {
        if (target == nums[c2]) r2 = c2 - 1;
        else l2 = c2 + 1;
        c2 = l2 + r2 >> 1;
    }
    ans[0] = c2;
    
    l2 = c;
    r2 = r;
    c2 = l2 + r2 >> 1;
    while (nums[c2] != target || (c2 < r2 && nums[c2+1] == target)) {
        if (target == nums[c2]) l2 = c2 + 1;
        else r2 = c2 - 1;
        c2 = l2 + r2 >> 1;
    }
    ans[1] = c2;
    
    return ans;
};