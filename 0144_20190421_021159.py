# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        stack = [root]
        res = []
        # while stack:
#             if stack[-1].left:
#                 stack.append(stack[-1].left)
#                 res.append(stack[-1].val)
#             else:
#                 n = stack.pop()
#                 while stack and not n.right:
#                     n = stack.pop()
#                 if n.right:
#                     stack.append(n.right)
#                     res.append(stack[-1].val)
        while stack:
            n = stack.pop()
            res.append(n.val)
            if n.right:
                stack.append(n.right)
            if n.left:
                stack.append(n.left)
        return res
    
            