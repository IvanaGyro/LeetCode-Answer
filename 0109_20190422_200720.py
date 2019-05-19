# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        slow, fast, prev = head, head, None
        while fast.next and fast.next.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        root = TreeNode(slow.val)
        root.right = self.sortedListToBST(slow.next)
        if prev:
            prev.next = None
            root.left = self.sortedListToBST(head)
        return root
        