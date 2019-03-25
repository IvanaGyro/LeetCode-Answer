/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function(nums) {
    var swap = function (a, b, nums) {
        let tmp = nums[a];
        nums[a] = nums[b];
        nums[b] = tmp;
    }
    
    var reverse = function (start, nums) {
        for (let i = start; i < ((start+nums.length) >> 1); ++i) {
            let j = (nums.length - 1) - (i - start);
            var tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
        }
    }
    
    for (let i = nums.length - 1; i > 0; --i) {
        if (nums[i] > nums[i-1]) {
            let l = i, r = nums.length, c = ((l+r) >> 1);
            while (nums[c] <= nums[i-1] || (c != nums.length-1 && nums[c+1] > nums[i-1])) {
                if (nums[c] <= nums[i-1]) {
                    r = c - 1;
                } else {
                    l = c + 1;
                }
                c = ((l+r) >> 1);
            }
            swap(c, i-1, nums);
            reverse(i, nums);
            return;
        }
    }
    reverse(0, nums);
    return;
};