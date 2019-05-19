"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        from collections import defaultdict
        
        def new_node():
            return Node(None, None, None)
        
        visited = defaultdict(new_node)
        
        def get_new_node(node):
            if not node:
                return None
            return visited[node]
        
        nhead = get_new_node(head) 
        nptr, ptr = nhead, head
        
        while ptr:
            nptr.val = ptr.val
            nptr.random = get_new_node(ptr.random)
            nptr.next = get_new_node(ptr.next)
            ptr = ptr.next
            nptr = nptr.next
        return nhead
            
            
        