# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        next_queue = []
        res = []
        
        def helper(node):
            if node.left is not None:
                next_queue.append(node.left)
            if node.right is not None:
                next_queue.append(node.right)
            return node.val
        
        while queue:
            res.append([helper(n) for n in queue])
            queue = next_queue
            next_queue = []
            
        return res