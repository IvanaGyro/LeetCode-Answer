# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None
        root = TreeNode(postorder.pop())
        stack = [root]
        i = len(inorder) - 1
        for n in reversed(postorder):
            if inorder[i] == stack[-1].val:
                while stack and inorder[i] == stack[-1].val:
                    i -= 1
                    prev = stack.pop()
                prev.left = TreeNode(n)
                stack.append(prev.left)
            else:
                stack[-1].right = TreeNode(n)
                stack.append(stack[-1].right)
        
        return root