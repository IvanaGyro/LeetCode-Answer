class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        lengths = collections.defaultdict(dict)
        max_len = 0
        
        for i in range(len(A)):
            cur = A[i]
            for step in lengths[cur]:
                length = lengths[cur][step] + 1
                lengths[cur + step][step] = length
                max_len = max(max_len, length)

            for j in range(i):
                past = A[j]
                step = cur - past
                if step not in lengths[cur + step]:
                    lengths[cur + step][step] = 2
                    max_len = max(max_len, 2)
                
        return max_len
                