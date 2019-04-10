# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 0:
            return head
        dummy = ListNode(0)
        dummy.next = head
        lptr = rptr = dummy
        k_ = k
        cnt = 0
        while rptr.next is not None and k_:
            cnt += 1
            rptr = rptr.next
            k_ -= 1
        
        if rptr.next is None:
            k %= cnt
            lptr = rptr = dummy
            for i in range(k):
                rptr = rptr.next
        
        while rptr.next is not None:
            rptr = rptr.next
            lptr = lptr.next
        rptr.next = head
        head = lptr.next
        lptr.next = None
        return head
        