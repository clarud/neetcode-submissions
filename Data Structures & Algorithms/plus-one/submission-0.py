class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        res = []
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            carry = 0
            if digits[i] >= 10:
                digits[i] %= 10
                carry = 1
            res.append(digits[i])
        if carry == 1:
            res.append(carry)
        return list(reversed(res))

            