/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

var reverseList = function (head) {
    if (!head) return null;
    
    var last = null, cur = head, next = cur.next;
    var newTail = head, newHead;
    while (cur) {
        cur.next = last;
        last = cur;
        cur = next;
        if (next)
            next = next.next;
    }
    newHead = last;
    return [newHead, newTail];
}

/**
 * @param {ListNode} head
 * @param {number} m
 * @param {number} n
 * @return {ListNode}
 */
var reverseBetween = function(head, m, n) {
    if (m == n) return head;
    
    var next, last;
    var subHead, subTail;
    
    if (m == 1) {
        last = null;
        subHead = head;
    } else {
        last = head;
        for (var i = 1; i < m - 1; ++i)
            last = last.next;
        subHead = last.next;
    }
    subTail = subHead;
    for (var i = 0; i < n - m; ++i)
        subTail = subTail.next;
    next = subTail.next;
    subTail.next = null;
    
    var newList = reverseList(subHead);
    
    newList[1].next = next;
    if (!last) return newList[0];
    last.next = newList[0];
    return head;
};