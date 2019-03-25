/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    var l = 0;
    for (let r = 0; r < nums.length; ++r) {
        if (nums[r] !== val) nums[l++] = nums[r];
    }
    return l;
};