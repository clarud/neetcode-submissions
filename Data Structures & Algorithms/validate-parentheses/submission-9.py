class Solution:
    def isValid(self, s: str) -> bool:
        op = {
            "{":"}",
            "[":"]", 
            "(":")"
            }
        stack = []
        for b in s:
            if b in op:
                stack.append(b)
            else:
                if not stack or op[stack[-1]] != b:
                    return False
                else:
                    stack.pop()
        return True if not stack else False

