# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:    
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        def traversal(root, lvl):
            if root is None:
                return
            if lvl == len(res):
                res.append(root.val)
            traversal(root.right, lvl+1)
            traversal(root.left, lvl+1)
        traversal(root, 0)
        return res
    