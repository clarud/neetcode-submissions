class Solution:
    def helper(self, index):
        if index == self.length:
            self.res.append(self.path[:])
            return

        for i in range(index, self.length):
            if self.is_pal[index][i]:
                self.path.append(self.s[index:i+1])
                self.helper(i + 1)
                self.path.pop()

    def partition(self, s: str) -> List[List[str]]:
        self.length = len(s)
        self.s = s
        self.is_pal = [[False] * self.length for _ in range(self.length)]
        for r in range(self.length):
            for l in range(r + 1):
                if s[l] == s[r] and (r - l <= 2 or self.is_pal[l + 1][r - 1]):
                    self.is_pal[l][r] = True
        self.res = []
        self.path = []
        self.helper(0)
        return self.res    