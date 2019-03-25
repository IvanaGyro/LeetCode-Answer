/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
    var dummy = new ListNode();
    var pointer = dummy;
    var tmp;
    while (l1 !== null && l2 !== null) {
        if (l1.val < l2.val){
            tmp = l1;
            l1 = l1.next;
        } else {
            tmp = l2;
            l2 = l2.next;
        }
        pointer.next = tmp;
        pointer = pointer.next;
    }
    tmp = l1 === null ? l2 : l1;
    pointer.next = tmp;
    return dummy.next;
};