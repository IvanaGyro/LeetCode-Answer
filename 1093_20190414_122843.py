# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        gen = self.get_node(S)
        _, num = next(gen)
        root = TreeNode(num)
        stack = [root]
        cur = stack[-1]
        for level, num in gen:
            while len(stack) > level:
                stack.pop()
            cur = stack[-1]   
            new = TreeNode(num)
            if cur.left is None:
                cur.left = new
                stack.append(cur.left)
            else:
                cur.right = new
                stack.append(cur.right)
        
        return root
        # res = [root.val]
        # queue = [root]
        # next_queue = []
        # while queue:
        #     for node in queue:
        #         if node.left is None:
        #             continue
        #         res.append(node.left.val)
        #         next_queue.append(node.left)
        #         if node.right is None:
        #             res.append(None)
        #             continue
        #         res.append(node.right.val)
        #         next_queue.append(node.right)
        #     queue = next_queue
        #     next_queue = []
        
        
    def get_node(self, S):
        level = 0
        i = 0
        while i < len(S):
            if S[i] == '-':
                level += 1
            else:
                num = ''
                while i < len(S) and S[i] != '-':
                    num += S[i]
                    i += 1
                i -= 1
                yield level, int(num)
                level = 0
            i += 1
            