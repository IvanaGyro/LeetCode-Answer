# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
       
        stack = [root]
        res = []
        prev = TreeNode(None)
        while stack:
            n = stack[-1]
            if not n.left and not n.right:
                prev = n
                res.append(stack.pop().val)
            elif n.left == prev or n.right == prev:
                prev = n
                res.append(stack.pop().val)
            else:
                if n.right:
                    stack.append(n.right)
                if n.left:
                    stack.append(n.left)
                
        return res

                