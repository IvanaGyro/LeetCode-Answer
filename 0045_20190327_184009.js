/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    var times = new Array(nums.length);
    times[0] = 0;
    var remain = 0;
    
    var update = function(i) {
        for (let j = 1; j <= nums[i]; ++j) {
            if (i + j >= times.length) break;
            if (times[i+j] === undefined) {
                times[i+j] = times[i] + 1;
            } else {
                times[i+j] = Math.min(times[i+j], times[i]+1);
            }
        }
        remain = i + nums[i];
    }
    
    update(0);
    for (let i = 1; i < nums.length; ++i) {
        if (i + nums[i] > remain) {
            update(i);
        }
    }
    return times[nums.length-1];
};