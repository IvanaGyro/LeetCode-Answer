/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var reverseKGroup = function(head, k) {
    if (k <= 1) return head;
    if (head === null) return head;
    
    var reverseGroup = function(dummy, tail) {
        var tmp = dummy.next;
        var head = tail;
        var newDummy = null;
        while (tmp !== tail) {
            dummy.next = dummy.next.next;
            tmp.next = head;
            head = tmp;
            tmp = dummy.next;
            if (newDummy === null) newDummy = head;
        }
        dummy.next = head;
        return newDummy;
    }
    
    var dummy = new ListNode();
    dummy.next = head;
    var pointer = dummy;
    var tail = pointer.next;
    
    while (true) {
        for (let i = k; i; --i) {
            if (tail === null) return dummy.next;
            tail = tail.next;
        }
        pointer = reverseGroup(pointer, tail);
    }


};