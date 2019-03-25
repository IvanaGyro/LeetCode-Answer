/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    if (!nums.length) return -1;
    
    var l = 0, 
        r = nums.length - 1, 
        c = l + r >> 1;
    while (nums[c] != target && l < r) {
        let state; // true: search left side, false: search rigth side
        if (nums[l] > nums[r]) {
            if (nums[c] >= nums[l]) {
                if (target < nums[c] && target >= nums[l]) state = true;
                else state = false;
            } else {
                if (target > nums[c] && target <= nums[r]) state = false;
                else state = true;
            }
        } else {
            if (target > nums[c]) state = false;
            else state = true;
        }
        if (state) {
            r = c - 1;
        } else {
            l = c + 1;
        }
        c = l + r >> 1;
    }
    if (nums[c] == target) return c;
    else return -1;
};

var search_test = function() {
    var n = 7, len = 5;
    var arr = Array(n);
    for (let i = 0; i < n; ++i) {
        arr[i] = i;
    }
    for (let i = 0; i < n - len; ++i) {
        arr[Math.floor(Math.random()*(n - i))] = undefined;
    }
    arr = arr.filter(val => val !== undefined);
    arr = arr.concat(arr);
    for (let i = 0; i < len; ++i) {
        let nums = arr.slice(i, i + len);
        for (let target = 0; target < n; ++target) {
            let result = search_(nums, target);
            console.log('nums = ' + nums + ', target = ' + target + ', output = ' + result);
        }
    }   
}