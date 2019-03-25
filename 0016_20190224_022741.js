/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    if (nums.length == 3) return nums.reduce((partial_sum, a) => partial_sum + a);
    var result = nums[0] + nums[1] + nums[2];
    var minDiff = Math.abs(result - target);
    for (var i = 0; i < nums.length-2; ++i) {
        for (var j = i + 1; j < nums.length-1; ++j) {
            for (var k = j + 1; k < nums.length; ++k) {
                const sum = nums[i] + nums[j] + nums[k];
                const diff = Math.abs(sum - target);
                if (diff < minDiff) {
                    minDiff = diff;
                    result = sum;
                }
            }
        }
    }
    return result;
};