from bisect import insort
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        INT_MAX = (1 << 32) - 1
        stack = [(0, 0, INT_MAX)]
        res = []
        for l, r, h in buildings:
            if l == r:
                continue
            while stack[-1][2] <= l:
                ch, cl, cr = stack.pop()
                while stack[-1][2] <= cr:
                    stack.pop()
                new_h = stack[-1][0]
                if l > cr or h <= new_h:
                    res.append([cr, new_h])
            if h >= stack[-1][0]:
                if not res:
                    res.append([l, h])
                elif h != res[-1][1]:
                    if l == res[-1][0]:
                        res.pop()
                    res.append([l, h])
                stack.append((h, l, r))
            else:
                insort(stack, (h, l, r))
        while len(stack) > 1:
            h, l, r = stack.pop()
            while stack and stack[-1][2] <= r:
                stack.pop()
            new_h = stack[-1][0] if stack else 0
            res.append([r, new_h])
        return res
    