class Solution:
    def calculate(self, s: str) -> int:
        nums = []
        oprs = []
        num = 0
        for c in s:
            if c == ' ':
                continue
            elif ord('0') <= ord(c) <= ord('9'):
                num = num*10 + ord(c) - ord('0')
            else:
                nums.append(num)
                num = 0
                if oprs:
                    op = oprs.pop()
                    if op == '*':
                        nums.append(nums.pop() * nums.pop())
                    elif op == '/':
                        a = nums.pop()
                        b = nums.pop()
                        nums.append(b // a)
                    else:
                        oprs.append(op)
                oprs.append(c)
        if oprs:
            if oprs[-1] == '*':
                nums[-1] *= num
                oprs.pop()
            elif oprs[-1] == '/':
                nums[-1] //= num
                oprs.pop()
            else:
                nums.append(num)
        else:
            nums.append(num)
        num = nums[0]
        for i in range(1, len(nums)):
            op = oprs[i-1]
            if op == '+':
                num += nums[i]
            elif op == '-':
                num -= nums[i]
        return num
    
            
                                