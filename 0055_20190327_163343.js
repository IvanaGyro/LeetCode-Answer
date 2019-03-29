/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    var can = new Array(nums.length);
    var jump = function(idx) {
        if (idx == 0) return true;
        for (let i = 1; i <= idx; ++i) {
            if (nums[idx-i] >= i) {
                if (can[idx-i] !== undefined) return can[idx-i];
                if (jump(idx-i)){
                    can[idx-i] = true;
                    return true;
                };
            } else {
                can[idx-i] = false;
            }
        }
        can[idx] = false;
        return false;
    }
    return jump(nums.length-1);
};
