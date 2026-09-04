class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operand_set = set(["+", "-", "*", "/"])
        def op(operand0, operand1, operation):
            print(f"{operand0} {operation} {operand1}")
            if operation == "+":
                return operand0 + operand1
            elif operation == "-":
                return operand0 - operand1
            elif operation == "*":
                return operand0 * operand1
            elif operation == "/":
                return int(operand0 / operand1)
        for t in tokens:
            if t in operand_set:
                operands = []
                while stack and len(operands) < 2:
                    operand = stack.pop()
                    operands.append(int(operand))
                stack.append(op(operands[1], operands[0], t))
            else:
                stack.append(int(t))
        return stack.pop()