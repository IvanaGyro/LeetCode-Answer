/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    var cur = head;
    var end, l, r;
    if (!head) return true;
    while (cur.next) {
        cur.next.prev = cur;
        cur = cur.next;
    }
    end = cur;
    l = head;
    r= end;
    while (l != r && l.prev != r) {
        if (l.val != r.val) return false;
        l = l.next;
        r = r.prev;
    }
    return true;
};