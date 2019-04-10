class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        if N < 10:
            return N
        a = []
        while N:
            a.append(N % 10)
            N //= 10
        
        def build_num(r):
            ans = 0
            for i in range(len(a)-1, r-1, -1):
                ans *= 10
                ans += a[i]
            ans *= (10 ** r)
            return ans - 1
        
        r = len(a) - 1
        for l in range(len(a)-1, 0, -1):
            if a[l-1] < a[l]:
                return build_num(r)
            elif a[l-1] > a[l]:
                r = l - 1
        return build_num(0) + 1