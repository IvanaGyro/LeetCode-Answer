# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        root = TreeNode(None)
        self.build(root, nums, 0, len(nums))
        return root
    
    def build(self, root, nums, l, r):
        i = (l + r - 1) >> 1
        root.val = nums[i]
        if i > l:
            root.left = TreeNode(None)
            self.build(root.left, nums, l, i)
        if i < r - 1:
            root.right = TreeNode(None)
            self.build(root.right, nums, i + 1, r)