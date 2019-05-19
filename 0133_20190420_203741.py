"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        new_node = Node(None, None)
        queue = [node]
        new_queue = [new_node]
        visited = set()
        id_table = {id(node): new_node}
        while queue:
            for _ in range(len(queue)):
                origin = queue.pop(0)
                copyed = new_queue.pop(0)
                if id(origin) in visited:
                    continue
                neighbors = []
                for neighbor in origin.neighbors:
                    n_id = id(neighbor)
                    if n_id not in id_table:
                        id_table[n_id] = Node(None, None)
                    neighbors.append(id_table[n_id])
                    if n_id not in visited:
                        queue.append(neighbor)
                        new_queue.append(id_table[n_id])
                copyed.neighbors = neighbors
                copyed.val = origin.val
                visited.add(id(origin))
        return new_node