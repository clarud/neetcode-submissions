class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def is_op(op):
            return op in {"+", "-", "*", "/"}
        def operation(op, n1, n2):
            if op == "+":
                return n1 + n2
            elif op == "-":
                return n1 - n2
            elif op == "*":
                return n1 * n2
            elif op == "/":
                if n2 == 0:
                    return n1
                return int(n1 / n2)
                
        for t in tokens:
            if is_op(t):
                if len(stack) < 2:
                    return -1
                op1, op2 = stack.pop(), stack.pop()
                stack.append(int(eval(str(op2) + t + str(op1))))
            else:
                stack.append(int(t))
        return stack.pop() if stack else -1



