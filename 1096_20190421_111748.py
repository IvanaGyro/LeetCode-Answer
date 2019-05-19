class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        if len(A) < L + M:
            return 0
        Ls, Ms = [0]*len(A), [0]*len(A)
        Ls[L - 1] = sum(A[:L])
        Ms[M - 1] = sum(A[:M])
        for i in range(L, len(A)):
            Ls[i] = Ls[i - 1] + A[i] - A[i - L]
        for i in range(M, len(A)):
            Ms[i] = Ms[i - 1] + A[i] - A[i - M]
        
        max1 = max([Ls[i] + Ms[j] for i in range(L-1, len(A) - M) for j in range(i + M, len(A))])
        if L != M:
            max2 = max([Ms[i] + Ls[j] for i in range(M-1, len(A) - L) for j in range(i + L, len(A))])
        else:
            max2 = 0
        return max(max1, max2)
    