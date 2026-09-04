class Solution:
    def helper(self, index, curr):
        if len(curr) == self.length and self.digits != "":
            self.res.append(curr[:])
            return
        for i in range(index, self.length):
            dig = int(self.digits[i])
            for j in range(len(self.digit_dict[dig])):
                curr += self.digit_dict[dig][j]
                self.helper(i + 1, curr)
                curr = curr[:-1]

    def letterCombinations(self, digits: str) -> List[str]:
        self.digit_dict = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
            }
        self.digits = digits
        self.length = len(digits)
        self.res = []
        self.helper(0, "")
        return self.res

