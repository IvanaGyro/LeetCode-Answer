# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None:
            return None
        sp = sdummy = ListNode(None)
        bp = bdummy = ListNode(None)
        cur = head
        while cur:
            if cur.val < x:
                sp.next = cur
                sp = sp.next
            else:
                bp.next = cur
                bp = bp.next
            cur = cur.next
        sp.next = bdummy.next
        bp.next = None
        return sdummy.next
        