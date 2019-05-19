# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        total = 0
        
        def dfs(root, curSum):
            nonlocal total
            if not root:
                return
            curSum = curSum * 10 + root.val
            if not root.left and not root.right:
                total += curSum
            else:
                dfs(root.left, curSum)
                dfs(root.right, curSum)
                
        dfs(root, 0)
        return total
    