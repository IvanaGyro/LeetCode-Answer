# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        arr = []
        ptr = head
        while ptr:
            arr.append(ptr)
            ptr = ptr.next
        l, r = 0, len(arr) - 1
        reorder = []
        while l < r:
            reorder.append(arr[l])
            reorder.append(arr[r])
            l += 1
            r -= 1
        if l == r:
            reorder.append(arr[l])
        reorder.append(None)
        for i in range(1, len(reorder)):
            reorder[i - 1].next = reorder[i]
            