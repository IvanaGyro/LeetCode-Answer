class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        arr = ["1"]
        tmp = []
        for i in range(n-1):
            cur = arr[0]
            cnt = 1
            for j in range(1, len(arr)):
                if cur != arr[j]:
                    tmp.append(str(cnt))
                    tmp.append(cur)
                    cur = arr[j]
                    cnt = 1
                else:
                    cnt += 1
            tmp.append(str(cnt))
            tmp.append(cur)
            arr = tmp
            tmp = []
        return "".join(arr)
