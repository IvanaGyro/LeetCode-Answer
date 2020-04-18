# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque([root])
        cnt = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                cnt += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return cnt
        