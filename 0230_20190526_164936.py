# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        k -= 1
        if not root:
            return None
        # p = root
        # while p.left:
        #     k += 1
        #     p = p.left
        
        def dfs(root):
            nonlocal k
            if root.left:
                res = dfs(root.left)
                if res is not None:
                    return res
            if k == 0:
                return root.val
            k -= 1
            if root.right:
                res = dfs(root.right)
                if res is not None:
                    return res
            return None
        return dfs(root)
    