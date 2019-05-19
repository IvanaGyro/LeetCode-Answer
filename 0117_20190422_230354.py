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
        if not root:
            return None
        ptr = pptr = root
        while ptr:
            prev = ptr = None
            while pptr:
                if pptr.left or pptr.right:
                    if prev:
                        prev.next = pptr.left if pptr.left else pptr.right
                    else:
                        ptr = pptr.left if pptr.left else pptr.right
                    prev = pptr.right if pptr.right else pptr.left
                    if pptr.left and pptr.right:
                        pptr.left.next = pptr.right
                pptr = pptr.next
            pptr = ptr
        return root
                    
                