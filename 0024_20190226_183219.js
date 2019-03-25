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
var swapPairs = function(head) {
    if (head === null) return head;
    var pointer = head;
    var dummy = new ListNode();
    var last = dummy;
    last.next = head;
    while (pointer && pointer.next) {
        let tmp = pointer.next;
        pointer.next = pointer.next.next;
        tmp.next = pointer;
        last.next = tmp;
        last = pointer;
        pointer = pointer.next;
    }
    return dummy.next;
};
