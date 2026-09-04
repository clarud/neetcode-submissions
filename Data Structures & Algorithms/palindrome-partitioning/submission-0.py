class Solution:
    def is_palindrome(self, string):
        return string == string[::-1]

    def helper(self, index, curr, s):
        if index == self.length:
            self.res.append(curr[:])
            return

        for i in range(index, self.length):
            if self.is_palindrome(s[index:i+1]):
                curr.append(s[index:i+1])
                self.helper(i + 1, curr[:], s[:])
                curr.pop()

    def partition(self, s: str) -> List[List[str]]:
        self.length = len(s)
        self.s = s
        self.res = []
        self.helper(0, [], s[:])
        return self.res    