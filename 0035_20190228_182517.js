/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    if (!nums.length) return 0;
    if (target < nums[0]) return 0;
    if (target > nums[nums.length-1]) return nums.length;
    
    var l = 0,
        r = nums.length - 1,
        c = l + r >> 1;
    while (nums[c] !== target && l < r) {
        if (target > nums[c]) l = c + 1;
        else r = c - 1;
        c = l + r >> 1;
    }
    if (nums[c] == target) return c;
    return target > nums[c] ? c + 1 : c;
};

var searchInsert_test = function () {
    var nums, target;
    
    var run = function (nums, target) {
        var result = searchInsert_(nums, target);
        console.log('nums = ' + nums + ', target = ' + target + ', result = ' + result);
    }
    
    nums = [1,3,5,6];
    for (let i = 0; i < 8; ++i) {
        run(nums, i);
    }
    
    nums = [1,3];
    for (let i = 0; i < 5; ++i) {
        run(nums, i);
    }
}