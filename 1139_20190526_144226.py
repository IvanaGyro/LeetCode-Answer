class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        if len(A) <= 1:
            return A
        n = len(A)
        for i in range(n-2, -1, -1):
            if A[i] > A[i+1]:
                break
        else:
            return A
        for j in range(n-1, i, -1):
            if A[j] < A[i]:
                break
        while A[j-1] == A[j]:
            j -= 1
        A[i], A[j] = A[j], A[i]
        return A
    