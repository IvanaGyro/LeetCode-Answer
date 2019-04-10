class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        ans = [0]*(len(num1)+len(num2))
        for i in range(len(num1)-1, -1, -1):
            offset = len(num1) - 1 - i
            for j in range(len(num2)-1, -1, -1):
                m = int(num1[i]) * int(num2[j])
                carry, remain = m // 10, m % 10
                ans[offset] += remain
                if ans[offset] >= 10:
                    carry += 1
                    ans[offset] -= 10
                idx = offset + 1
                while carry:
                    ans[idx] += carry
                    if ans[idx] >= 10:
                        carry = 1
                        ans[idx] -= 10
                    else:
                        carry = 0
                    idx += 1
                offset += 1
        
        for i in range(len(ans)-1, -1, -1):
            if ans[i] != 0:
                break 
        ans = ans[:i+1]
        ans.reverse()
        return "".join(map(lambda n: str(n), ans))