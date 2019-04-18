# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder.pop(0))
        stack = [root]
        i = 0
        for n in preorder:
            if stack and stack[-1].val == inorder[i]:
                while stack and stack[-1].val == inorder[i]:
                    prev = stack.pop()
                    i += 1
                prev.right = TreeNode(n)
                stack.append(prev.right)
            else:
                stack[-1].left = TreeNode(n)
                stack.append(stack[-1].left)
        return root
            
        
            