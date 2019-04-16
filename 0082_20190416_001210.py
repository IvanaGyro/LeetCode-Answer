# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        dummy = ListNode(None)
        dummy.next = head
        l = dummy
        r = head
        cnt = 1
        while r.next is not None:
            if r.next.val != r.val:
                if cnt > 1:
                    l.next = r.next 
                else:
                    l = r
                cnt = 0
            r = r.next
            cnt += 1
        if cnt > 1:
            l.next = None
        return dummy.next