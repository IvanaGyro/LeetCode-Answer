class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in '+-*/':
                b = stack.pop()
                a = stack.pop()
                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(a - b)
                elif t == '*':
                    stack.append(a * b)
                elif t == '/':
                    neg = False
                    if a < 0 and b < 0:
                        a, b = -a, -b
                    elif a < 0:
                        neg = True
                        a = -a
                    elif b < 0:
                        neg = True
                        b = -b
                    stack.append(a // b * (-1 if neg else 1))
            else:
                stack.append(int(t))
        return stack[-1]
                