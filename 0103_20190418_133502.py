# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        q = [root]
        nq = []
        res = []
        state = 1
        while q:
            ns = []
            for n in range(len(q)):
                ns.append(q[n].val)
                if state and q[~n].right is not None:
                    nq.append(q[~n].right)
                if q[~n].left is not None:
                    nq.append(q[~n].left)
                if not state and q[~n].right is not None:
                    nq.append(q[~n].right)
            res.append(ns)
            state ^= 1
            q = nq
            nq = []
            
        return res
                
        