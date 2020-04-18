# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        ptr = dummy = ListNode(None)
        dummy.next = head
        while ptr.next:
            if ptr.next.val == val:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return dummy.next
    