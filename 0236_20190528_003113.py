# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        
        def is_found(s1, s2, node):
            nonlocal res
            if res is not None:
                return True
            s1[0], s1[1] = s1[0] or s2[0], s1[1] or s2[1]
            if s1[0] and s1[1]:
                res = node
                return True
            return False
        
        def dfs(root):
            if not root:
                return False, False
            state = [root == p, root == q]
            if is_found(state, dfs(root.left), root):
                return True, True
            if is_found(state, dfs(root.right), root):
                return True, True
            return state
        dfs(root)
        return res