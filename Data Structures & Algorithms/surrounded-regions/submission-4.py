class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = [[0] * len(board[0]) for i in range(len(board))]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def is_edge(x, y):
            return x == 0 or x == len(board) - 1 or y == 0 or y == len(board[0]) - 1

        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col == "X":
                    visited[i][j] = 1
        q = deque()
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if visited[i][j] == 1:
                    continue
                if not is_edge(i, j):
                    continue
                q.append((i, j))
                visited[i][j] = 1
                board[i][j] = "#"
                while q:
                    curri, currj = q.popleft()
                    for addi, addj in directions:
                        nexti, nextj = curri + addi, currj + addj
                        if 0 <= nexti <= len(board) - 1 and 0 <= nextj <= len(board[0]) - 1 and not visited[nexti][nextj] and board[nexti][nextj] == "O":
                            q.append((nexti, nextj))
                            visited[nexti][nextj] = 1
                            board[nexti][nextj] = "#"
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col == "O":
                    board[i][j] = "X"
                if col == "#":
                    board[i][j] = "O"
            
