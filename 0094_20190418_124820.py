# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(v):
            if v is None:
                return
            dfs(v.left)
            res.append(v.val)
            dfs(v.right)
        
        dfs(root)
        return res