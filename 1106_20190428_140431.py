from collections import deque
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if source in blocked or target in blocked:
            return False
        if len(blocked) < 2:
            return True
        
        blocked = set((x, y) for x, y in blocked)
        
        # walls = []
        # off = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i != 0 or j != 0]
        # while blocked:
        #     wall = set()
        #     queue = deque((blocked.pop(),))
        #     while queue:
        #         for _ in range(len(queue)):
        #             x, y = queue.popleft()
        #             wall.add((x, y))
        #             for i, j in off:
        #                 if (x + i, y + j) in blocked:
        #                     blocked.remove((x + i, y + j))
        #                     queue.append((x + i, y + j))
        #     walls.append(wall)
        # for wall in walls:
        
        visited = set()
        actions = [(1, 0), (0 ,1), (-1, 0), (0, -1)]
        def flood(x, y):
            if [x, y] == target:
                return True
            if len(visited) > 19900:
                return True
            if x < 0 or y < 0 or x == 1000000 or y == 1000000:
                return False
            if (x, y) in visited or (x, y) in blocked:
                return False
            visited.add((x, y))
            dist = [(0, target[0] - x), (1, target[1] - y), (2, x - target[0]), (3, y - target[1])]
            dist.sort(key=lambda x: x[1], reverse=True)
            for d in dist:
                x_off, y_off = actions[d[0]]
                if flood(x + x_off, y + y_off):
                    return True
            return False
        
        res = flood(*source)
        source, target = target, source
        visited = set()
        return res and flood(*source)

            