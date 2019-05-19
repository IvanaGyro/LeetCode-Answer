from collections import defaultdict
from math import inf
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        if not rectangles:
            return False
    
        counter = defaultdict(int)
        area = 0
        min_x, min_y, max_x, max_y = inf, inf, -inf, -inf
        
        for x1, y1, x2, y2 in rectangles:
            if x2 <= x1 or y2 <= y1:
                continue
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)
            for key, pos in enumerate([(x1, y1), (x2, y1), (x1, y2), (x2, y2)]):
                mask = 1 << key
                if counter[pos] & mask:
                    return False
                counter[pos] |= mask
            area += (x2 - x1) * (y2 - y1)
        
        if area != (max_x - min_x) * (max_y - min_y):
            return False
        
        valid_state = [0b0011, 0b0101, 0b1010, 0b1100, 0b1111]

        
        if counter[(min_x, min_y)] != 0b0001:
                    return False
        if counter[(max_x, min_y)] != 0b0010:
                    return False
        if counter[(min_x, max_y)] != 0b0100:
                    return False
        if counter[(max_x, max_y)] != 0b1000:
                    return False
        del counter[(min_x, min_y)], counter[(max_x, min_y)], counter[(min_x, max_y)], counter[(max_x, max_y)]

        for pos in counter:
            if counter[pos] not in valid_state:
                return False
        
        return True
