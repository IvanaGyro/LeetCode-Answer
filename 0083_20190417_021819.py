# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = dummy = ListNode(None)
        cur = head
        while cur:
            if cur.val != p.val:
                p.next = cur
                p = p.next
            cur = cur.next
        p.next = None
        return dummy.next