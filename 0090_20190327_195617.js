/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function(nums) {
    var table = {};
    nums.forEach((val)=>{
        if (table[val] === undefined) {
            table[val] = 1;
        } else {
            ++table[val];
        }
    });
    var result = [[]];
    for (key in table) {
        let tmp = [];
        let cur;
        while ((cur = result.pop()) !== undefined) {
            for (let i = 0; i <= table[key]; ++i) {
                tmp.push(cur.concat(new Array(i).fill(key)));
            }
        }
        result = tmp;
    }
    return result;
};