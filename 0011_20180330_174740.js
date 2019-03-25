/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    var max = 0, l = 0, r = height.length-1;
    while (l != r) {
        var area = Math.min(height[l], height[r])*(r-l);
        if (area > max) {
            max = area;
        }
        if (height[r] < height[l]) --r;
        else ++l;
    }
    return max;
};