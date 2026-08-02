class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s == "+":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op1+op2)
            elif s == "*":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op1*op2)
            elif s == "-":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2-op1)
            elif s == "/":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(float(op2)/op1))
            else:
                stack.append(int(s))
        return stack[0]