from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = defaultdict(set)
        for p in prerequisites:
            edges[p[0]].add(p[1])
        
        visited = set()
        path = set()
        
        def traversal(course):
            if course in path:
                return False
            visited.add(course)
            path.add(course)
            if course in edges:
                for req in edges[course]:
                    if not traversal(req):
                        return False
            path.remove(course)
            return True
        
        for course in edges:
            if course not in visited:
                if not traversal(course):
                    return False
        return True
    