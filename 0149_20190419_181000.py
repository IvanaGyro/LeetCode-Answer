class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        if len(points) == 1:
            return 1
        from collections import defaultdict, Counter
        from math import gcd
        from bisect import bisect
        tablex = defaultdict(list)
        tabley = defaultdict(int)
        counter = {}
        
        for p in points:
            tablex[p[0]].append(p[1])
            tabley[p[1]] += 1
        for x in tablex:
            tablex[x] = Counter(tablex[x])
            
            
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if points[i] == points[j]:
                    continue
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                if dx == 0:
                    if (0, 0, points[i][0], 0) not in counter:
                        counter[(0, 0, points[i][0], 0)] = sum(tablex[points[i][0]].values())
                elif dy == 0:
                    if (0, 0, 0, points[i][1]) not in counter:
                        counter[(0, 0, 0, points[i][1])] = tabley[points[i][1]]
                else:
                    c = gcd(dx, dy)
                    xi, yi = points[i][0], points[i][1]
                    dx //= c
                    dy //= c
                    
                    if dy < 0:
                        dx = -dx
                        dy = -dy
                    mx = xi - yi // dy * dx
                    my = yi - yi // dy * dy                                   
                    if (dx, dy, mx, my) in counter:
                        continue
                     
                    cnt = 0
                    for x in tablex:
                        if (x - xi) % dx == 0:
                            y = yi + (x - xi) // dx * dy
                        cnt += tablex[x][y]
                    counter[(dx, dy, mx, my)] = cnt


        return len(counter) and max(counter.values()) or len(points)
                