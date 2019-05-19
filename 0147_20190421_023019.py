# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        dummy = ListNode(None)
        dummy.next = head
        ptr = head
        while ptr.next:
            if ptr.next.val < ptr.val:
                pptr = ptr.next
                ptr.next = ptr.next.next
                ppptr = dummy
                while ppptr.next.val < pptr.val:
                    ppptr = ppptr.next
                pptr.next = ppptr.next
                ppptr.next = pptr
            else:
                ptr = ptr.next
            
        return dummy.next
            