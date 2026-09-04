class Solution:
    def is_palindrome(self, string):
        return string == string[::-1]

    def helper(self, index):
        if index == self.length:
            self.res.append(self.path[:])
            return

        for i in range(index, self.length):
            if self.is_palindrome(self.s[index:i+1]):
                self.path.append(self.s[index:i+1])
                self.helper(i + 1)
                self.path.pop()

    def partition(self, s: str) -> List[List[str]]:
        self.length = len(s)
        self.s = s
        self.res = []
        self.path = []
        self.helper(0)
        return self.res    