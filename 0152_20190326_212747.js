/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    if (nums.length == 0) return 0;
    if (nums.length == 1) return nums[0];
    var max = -Infinity,
        product = 1,
        l = 0,
        r = 0;
    while (r < nums.length) {
        if (nums[r] != 0) {
            product *= nums[r++];
            max = Math.max(max, product);
        } else {
            if (product < 0) {
                while (l < r & product < 0) {
                    product /= nums[l++];
                    console.log(product);
                }
            }
            if (l < r) {
                max = Math.max(max, product);
            } else {
                max = Math.max(max, 0);
            }
            r++;
            l = r;
            product = 1;
        } 
    }
    if (product < 0) {
        while (l < r & product < 0) {
            product /= nums[l++];
        }
        if (l < r) {
            max = Math.max(max, product);
        }
    }
    return max;
};