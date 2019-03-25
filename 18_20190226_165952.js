/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
    console.log(nums.sort(function(a,b){return a - b}));
    if (nums.length < 4) return [];
    var ans = [];
    for (let i = 0; i < nums.length-3; ++i) {
        for (let j = i + 1; j < nums.length-2; ++j) {
            for (let k = j + 1; k < nums.length-1; ++k) {
                let remain = target - nums[i] - nums[j] - nums[k];
                if (k < nums.length - 2 && remain < nums[k + 1]) break;
                if (remain > nums[nums.length - 1]) continue;
                let p = (k + nums.length) >> 1;
                let l = k, r = nums.length;
                while (nums[p] != remain &&
                        (
                            (p > k + 1 && nums[p-1] >= remain) || 
                            (p < nums.length - 1 && nums[p+1] <= remain)
                    )) 
                {
                    if (nums[p] < remain && p < nums.length - 1) {
                        l = p;
                        p = (p + r) >> 1;
                    } else { // nums[p] > remain
                        r = p;
                        p = (p + l) >> 1;
                    }
                }
                if (nums[p] == remain) {
                    ans.push([nums[i], nums[j], nums[k], nums[p]]);
                }
                while (nums[k + 1] == nums[k]) ++k;
            }
            while (nums[j + 1] == nums[j]) ++j;
        }
        while (nums[i + 1] == nums[i]) ++i;
    }
    return ans;
};