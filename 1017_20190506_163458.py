from math import inf
class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        if not A:
            return 0
        odd = [None]*len(A)
        even = [None]*len(A)
        odd[-1] = True
        even[-1] = True
        for i in reversed(range(len(A) - 1)):    
            n_min, r_min, n_max, r_max = inf, False, -inf, False
            for j in range(i+1, len(A)):
                if A[i] <= A[j] < n_min:
                    n_min, r_min = A[j], even[j]
                if A[i] >= A[j] > n_max:
                    n_max, r_max = A[j], odd[j]
            odd[i] = r_min
            even[i] = r_max
        return sum(odd)
    