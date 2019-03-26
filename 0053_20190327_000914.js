/**
 * @param {number[]} nums
 * @return {number}
 */
var _maxSubArray = function(nums) {
    if (nums.length == 0) return 0;
    if (nums.length == 1) return nums[0];
    var max = nums[0],
        cur,
        i = 0;
    while (i < nums.length & nums[i] <= 0) {
        max = Math.max(max, nums[i++]);
    }
    if (i == nums.length) return max;
    
    var window_sum = 0;
    while (i < nums.length) {
        if (nums[i] >= 0) {
            window_sum += nums[i];
        } else {
            max = Math.max(max, window_sum);
            if (window_sum + nums[i] >= 0) {
                window_sum += nums[i];
            } else {
                window_sum = 0;
            }
        }
        ++i;
    }
    return Math.max(max, window_sum);
};

var test = false;
var maxSubArray = function(nums) {
    if (!test) {
        return _maxSubArray(nums);
    }
    var cases = [
        [[], 0],
        [[2], 2],
        [[1,2], 3],
        [[-2], -2],
        [[-5,-4,-3], -3],
        [[-2,0,5], 5],
        [[-2,0,-5], 0],
        [[-2,1,0,-3], 1],
        [[-2,1,-3,4,-1,2,1,-5,4], 6],
        [[-2,1,-3,4,-1,2,1,-5], 6],
        [[-2,1,-3,4,-1,2,1,-5,4,5], 10]
    ];
    cases.forEach(function(c) {
        var result = _maxSubArray(c[0]);
        if (result != c[1]) {
            console.log(c, result);
        }
    });
}