/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    if (!head) return null;
    var cur = head, next = head.next, last = null;
    while (cur) {
        cur.next = last;
        last = cur;
        cur = next;
        if (next)
            next = next.next;
    }
    return last;
};