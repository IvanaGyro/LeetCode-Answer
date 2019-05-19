# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int, path=[]) -> List[List[int]]:
        return [] if root is None else (root.left is None and root.right is None and sum == root.val and [path + [root.val]] or self.pathSum(root.left, sum - root.val, path + [root.val]) + self.pathSum(root.right, sum - root.val, path + [root.val]))