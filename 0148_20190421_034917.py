# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        head, _ = self.sort(head)
        return head
    
    def sort(self, head):
        if not head.next:
            return head, head
        
        pivot = head.val
        eqp = p = head
        second = p2 = head
        while p.next:
            if p.next.val < pivot:
                tmp = p.next
                p.next = p.next.next
                tmp.next = second
                second = tmp
            else:
                if eqp.val <= eqp.next.val:
                    eqp = eqp.next
                p = p.next
        
        head = head.next
        p2.next = None
        second, p2 = self.sort(second)
        
        if head:
            if eqp != p:   
                head, p = self.sort(head)
            p2.next = head
            p2 = p
            
        return second, p2
