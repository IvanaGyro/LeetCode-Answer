from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = [set() for _ in range(numCourses)]
        pre = [0] * numCourses
        visited = [0] * numCourses
               
        for p in prerequisites:
            courses[p[1]].add(p[0])
            pre[p[0]] += 1
            
        
        ans = []
        def dfs(c):
            if visited[c] == -1:
                return False
            if pre[c] > 0:
                pre[c] -= 1
            if pre[c] == 0:
                ans.append(c)
                visited[c] = -1
                for next_c in courses[c]:
                    if not dfs(next_c):
                        return False
                visited[c] = 1
            return True
        
        for course in range(numCourses):
            if pre[course] == 0 and visited[course] == 0:
                if not dfs(course):
                    return []
        return ans if len(ans) == numCourses else []
    