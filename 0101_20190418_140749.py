# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        lq = [root]
        rq = [root]
        
        while lq:
            for _ in range(len(lq)):
                ln = lq.pop(0)
                rn = rq.pop(0)
                if ln is None and rn is None:
                    continue
                if ln is None or rn is None:
                    return False
                if ln.val != rn.val:
                    return False
                lq.append(ln.left)
                lq.append(ln.right)
                rq.append(rn.right)
                rq.append(rn.left)
        return True