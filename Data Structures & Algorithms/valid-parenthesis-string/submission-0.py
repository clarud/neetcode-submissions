from collections import defaultdict
class Solution:
    def checkValidString(self, s: str) -> bool:
        paren_stack = []
        astr_stack = []
        for i, each in enumerate(s):
            if each == "(":
                paren_stack.append(i)
            if each == "*":
                astr_stack.append(i)
            if each == ")":
                if paren_stack:
                    paren_stack.pop()
                else:
                    if astr_stack:
                        astr_stack.pop()
                    else:
                        return False
        for i in range(min(len(paren_stack), len(astr_stack))):
            if paren_stack:
                paren_ind = paren_stack.pop()
            if astr_stack:
                astr_ind = astr_stack.pop()
            if paren_ind > astr_ind:
                return False
        return not paren_stack
