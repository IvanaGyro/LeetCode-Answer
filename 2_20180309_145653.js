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
var addTwoNumbers = function(l1, l2) {
    var head = l1;
    var carry;
    var check_carry = function () {
        if (l1.val >= 10) {
            l1.val -= 10;
            carry = 1;
        } else {
            carry = 0;
        }
    };
    l1.val = l1.val + l2.val;
    check_carry();
    while (l1.next !== null && l2.next !== null) {
        l1 = l1.next;
        l2 = l2.next;
        l1.val += l2.val + carry;
        check_carry();
    }
    if (l2.next !== null) {
        l1.next = l2.next;
    }
    while (carry) {
        if (l1.next === null) {
            l1.next = {
                val: 1,
                next: null
            }
            carry = 0;
        } else {
            l1 = l1.next;
            l1.val += carry;
            check_carry();
        }
    }
    return head;
};