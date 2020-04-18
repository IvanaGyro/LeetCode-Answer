from collections import Counter
import heapq
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = Counter(barcodes)
        res = []
        tasks = [(-t, -n) for n, t in counter.items()]
        heapq.heapify(tasks)
        while len(tasks) > 1:
            t_a, a = heapq.heappop(tasks)
            t_b, b = heapq.heappop(tasks)
            if res and res[-1] == -a:
                tmp_a, tmp_b = -b, -a
            else:
                tmp_a, tmp_b = -a, -b
            for i in range(-t_b):
                res.append(tmp_a)
                res.append(tmp_b)
            t_a -= t_b
            if t_a != 0:
                heapq.heappush(tasks, (t_a, a))
        if tasks:
            t_a, a = heapq.heappop(tasks)
            if t_a == -1 and (not res or res and res[-1] != -a):
                res.append(-a)
            else:
                j = 1
                for i in range(-t_a):
                    while res[j] == -a or res[j-1] == -a:
                        j += 1
                    res.insert(j, -a)
        return res
            