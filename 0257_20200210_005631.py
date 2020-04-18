# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = self.walk(root, [])
        return ['->'.join((str(n) for n in path)) for path in paths]
        
        
    def walk(self, root, path):
        if root is None:
            return []
        path = path + [root.val]
        return (self.walk(root.left, path) + self.walk(root.right, path)) or [path]
        