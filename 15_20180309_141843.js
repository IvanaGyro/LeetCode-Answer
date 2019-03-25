/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    var ans = [];
    var tmp = {};
    var cur = [];
    var dict = [];
    var nums2 = [];
    nums.map(function (val, idx, arr) {
        dict[val] = dict[val] === undefined ? 1 : dict[val] + 1;
        if (dict[val] <= 3) {
            nums2.push(val);
        }
    });
    nums = nums2;
    nums.sort(function (a, b) {return a - b;});
    dict = [];
    nums.map(function (val, idx, arr) {
        if (dict[val] === undefined) {
            dict[val] = [];
        }
        dict[val].push(idx);
    });
    console.log(nums.length);
    for(var i = 0; i < nums.length; ++i) {
        cur[0] = nums[i];
        if (cur[0] > 0) {
            break;
        }
        for(var j = i + 1; j < nums.length; ++j) {
            cur[1] = cur[0] + nums[j];
            if (cur[1] > 0) {
                break;
            }
            if (dict[-cur[1]] && dict[-cur[1]][dict[-cur[1]].length-1] > j) {
                var ans2 = [nums[i], nums[j], -cur[1]].sort();
                     if (tmp[ans2[0]] === undefined) {
                        tmp[ans2[0]] = {};
                    }
                    if (tmp[ans2[0]][ans2[1]] === undefined) {
                        tmp[ans2[0]][ans2[1]] = {};
                    }
                   if (tmp[ans2[0]][ans2[1]][ans2[2]] === undefined) {
                        tmp[ans2[0]][ans2[1]][ans2[2]] = {};
                    }
            }
            /*
            for (var k = j + 1; k < nums.length; ++k) {
                cur[2] = cur[1] + nums[k];
                if (cur[2] > 0) {
                     break;
                }
                if (cur[2] == 0) {
                    
                }
            }*/
        }
    }

    Object.keys(tmp).sort().map(function (val1, idx, arr) {
       Object.keys(tmp[val1]).sort().map(function (val2, idx, arr) {
            Object.keys(tmp[val1][val2]).sort().map(function (val3, idx, arr) {
        ans.push([parseInt(val1), parseInt(val2), parseInt(val3)]);
        }) ;
        }) ;
    });
    return ans;
};