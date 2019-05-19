# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        if not root:
            self.g = iter(())
            self.has_next = False
            self.cache = None
            return
        
        def g(root):
            if root.left:
                yield from g(root.left)
            yield root.val
            if root.right:
                yield from g(root.right)
        
        self.g = g(root)
        self.has_next = None
        self.cache = None

            
    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.cache is not None:
            v = self.cache
            self.cache = None
            self.has_next = None
        else:
            v = next(self.g, None)
        return v
                    

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.has_next is None:
            self.cache = next(self.g, None)
            if self.cache is None:
                self.has_next = False
            else:
                self.has_next = True
        return self.has_next


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()