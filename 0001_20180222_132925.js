/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  ans = [];  
  nums.forEach(function (val, idx, arr) {
      for(i = idx + 1; i<arr.length; ++i) {
          if (val + arr[i] === target) {
             ans.push(idx);
             ans.push(i);
              break;
          }
      }
  });
    return ans;
};