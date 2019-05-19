"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        def connect_children(root):
            if not root: return
            l, r = root.left, root.right
            while l and r:
                l.next = r
                l = l.right
                r = r.left
            connect_children(root.left)
            connect_children(root.right)

        connect_children(root)
        return root
            