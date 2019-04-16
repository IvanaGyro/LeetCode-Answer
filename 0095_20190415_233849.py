# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n:
            return [None]
        arr = [i for i in range(1, n+1)]
    
        return self.createSubTrees(arr)
        
    def createSubTrees(self, arr):
        if not arr:
            return [None]
        trees = []
        for i in range(len(arr)):
            l_trees = self.createSubTrees(arr[:i])
            r_trees = self.createSubTrees(arr[i+1:])
            
            for l in l_trees:
                for r in r_trees:
                    node = TreeNode(arr[i])
                    node.left = l
                    node.right = r
                    trees.append(node)
        return trees
