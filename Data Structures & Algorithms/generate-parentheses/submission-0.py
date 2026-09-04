class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def helper(opn, cls):
            if opn == cls == n:
                res.append("".join(stack))
                return
            if opn < n:
                stack.append("(")
                helper(opn + 1, cls)
                stack.pop()
            if cls < n and cls < opn:
                stack.append(")")
                helper(opn, cls + 1)
                stack.pop()
        
        helper(0, 0)
        return res
