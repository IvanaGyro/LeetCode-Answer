class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        avg = sum(A) / len(A)
        tb = [[None]*len(A) for i in range(len(A))]
        A.sort(key=lambda a: abs(a-avg))
        
        def dp(l, r):
            if l == r:
                return False
            
            if tb[l][r] is not None:
                return tb[l][r]
            if r - l <= 3:
                if r - l == 1:
                    tb[l][r] = A[l] == A[r]
                if r - l == 2:
                    tb[l][r] = A[l] + A[r] == A[l+1] or A[l] + A[l+1] == A[r]
                if r - l == 3:
                    tb[l][r] = A[l] + A[r] == A[l+1] + A[r-1] or A[l] + A[l+1] + A[r-1] == A[r]
                return tb[l][r]
            
            for i in range(l, r):
                r1 = dp(l, i)
                r2 = dp(i+1, r)
                if r1 and r2:
                    tb[l][r] = True
                    return True

        res = dp(0, len(A)-1)
        print(tb)
        return res
        
