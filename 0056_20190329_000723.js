/**
 * Definition for an interval.
 * function Interval(start, end) {
 *     this.start = start;
 *     this.end = end;
 * }
 */
/**
 * @param {Interval[]} intervals
 * @return {Interval[]}
 */
var merge = function(intervals) {
    if (intervals.length == 0) return [];
    intervals.sort((a, b)=>{
        return a.start - b.start;
    });
    var last = intervals[0],
        result = [last];
    for (let i = 1; i < intervals.length; ++i) {
            
        if (intervals[i].start <= last.end) {
            last.start = Math.min(intervals[i].start, last.start)
            last.end = Math.max(intervals[i].end, last.end);
        } else {
            last =intervals[i];
            result.push(last);
        }
    }
    return result;
};