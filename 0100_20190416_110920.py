# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        TreeNode.__eq__ = lambda s, other: s.val == other.val if other else other
                
        a_p = [p]
        a_q = [q]
        n_p = []
        n_q = []
        while a_p and a_q:
            if a_p == a_q:
                [(n_p.append(n.left), n_p.append(n.right)) for n in a_p if n]
                [(n_q.append(n.left), n_q.append(n.right)) for n in a_q if n]
                a_p = n_p
                a_q = n_q
                n_p = []
                n_q = []
            else:
                return False
        return not a_p and not a_q
            