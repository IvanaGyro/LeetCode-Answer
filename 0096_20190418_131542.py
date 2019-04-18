class Solution:
    def numTrees(self, n: int) -> int:
        tb = {}
        def dp(l, r):
            if (l, r) in tb:
                return tb[(l, r)]
            tb[(l ,r)] = 0
            for i in range(l, r):
                if i == l:
                    lcnt = 1
                else:
                    lcnt = dp(l, i)
                if i == r - 1:
                    rcnt = 1
                else:
                    rcnt = dp(i + 1, r)
                tb[(l, r)] += lcnt * rcnt
            return tb[(l, r)]
        dp(1, n + 1)
        return tb[(1, n + 1)]