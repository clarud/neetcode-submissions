class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  
        for t in tokens:
            if t in {"+", "-", "*", "/"}:
                if len(stack) < 2:
                    return -1
                op1, op2 = stack.pop(), stack.pop()
                stack.append(int(eval(str(op2) + t + str(op1))))
            else:
                stack.append(int(t))
        return stack.pop() if stack else -1



