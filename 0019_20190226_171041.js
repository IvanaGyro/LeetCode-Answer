/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    var right = head;
    while(--n) {
        right = right.next;
    }
    if (right.next === null) return head.next;
    right = right.next;
    var left = head;
    while (right.next !== null) {
        right = right.next;
        left = left.next;
    }
    left.next = left.next.next;
    return head;
};