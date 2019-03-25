/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    var l = 1;
    var cur = nums[0];
    for (let i = 1; i < nums.length; ++i) {
        if (nums[i] != cur) {
            nums[l++] = nums[i];
            cur = nums[i];
        }
    }
    return l;
};