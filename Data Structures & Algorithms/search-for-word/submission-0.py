class Solution:
    def dfs(self, row, col, index):
        if index == len(self.word):
            return True
        if (row < 0 or col < 0 or row >= self.rows or col >= self.cols or self.word[index] != self.board[row][col] or self.board[row][col] == '#'):
            return False

        self.board[row][col] = '#'
        res = (self.dfs(row + 1, col, index + 1) or
            self.dfs(row - 1, col, index + 1) or
            self.dfs(row, col + 1, index + 1) or
            self.dfs(row, col - 1, index + 1))
        self.board[row][col] = self.word[index]
        return res

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows, self.cols = len(board), len(board[0])
        self.word = word
        self.board = board

        for row in range(self.rows):
            for col in range(self.cols):
                if self.dfs(row, col, 0):
                    return True
        return False
