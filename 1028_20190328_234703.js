/**
 * Definition for an interval.
 * function Interval(start, end) {
 *     this.start = start;
 *     this.end = end;
 * }
 */
/**
 * @param {Interval[]} A
 * @param {Interval[]} B
 * @return {Interval[]}
 */
var intervalIntersection = function(A, B) {
    if (A.length == 0 || B.length == 0) return [];
    var pa = 0, ppa = 0, a = A[0].start,
        pb = 0, ppb = 0, b = B[0].start,
        cur = 0,
        result = [],
        interval = null;
    while ((pa < A.length || ppa == 1) && (pb < B.length || ppb == 1)) {
        if (a < b) {
            cur = a;
            if (ppa == 1) {
                ++pa;
                ppa = 0;
                if (pa < A.length) a = A[pa].start;
            } else {
                ppa = 1;
                a = A[pa].end;
            }
        } else {
            if (a == b && ppa == 0 && ppb == 1) {
                result.push(new Interval(a, b));
            }
            cur = b;
            if (ppb == 1) {
                ++pb;
                ppb = 0;
                if (pb < B.length) b = B[pb].start;
            } else {
                ppb = 1;
                b = B[pb].end;
            }
        }
        if (ppa & ppb) {
            interval = new Interval(cur, null);
        } else if (interval !== null) {
            interval.end = cur;
            result.push(interval);
            interval = null;
        }
    }
    return result;
};