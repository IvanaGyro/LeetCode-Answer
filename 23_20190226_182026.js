/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function(lists) {
    var dummy = new ListNode();
    var pointer = dummy;
    lists = lists.filter(list => list !== null);
    if (lists.length == 1) return lists[0];
    while (lists.length != 0) {
        let min = lists[0];
        let minIdx = 0;
        for (let i = 0; i < lists.length; ++i) {
            if (lists[i].val < min.val) {
                min = lists[i];
                minIdx = i;
            }
        }
        pointer.next = min;
        pointer = pointer.next;
        lists[minIdx] = lists[minIdx].next;
        if (lists[minIdx] === null) {
            lists.splice(minIdx, 1);
        }
    }
    return dummy.next;
};