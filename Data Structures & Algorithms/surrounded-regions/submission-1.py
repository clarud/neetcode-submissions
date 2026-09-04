class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = [[0] * len(board[0]) for i in range(len(board))]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col == "X":
                    visited[i][j] = 1
        q = deque()
        res = []
        yes = 1
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if visited[i][j] == 1:
                    continue
                q.append((i, j))
                yes = 1
                res = []
                while q:
                    curri, currj = q.popleft()
                    res.append((curri, currj))
                    for addi, addj in directions:
                        nexti, nextj = curri + addi, currj + addj
                        if 0 <= nexti <= len(board) - 1 and 0 <= nextj <= len(board[0]) - 1 and not visited[nexti][nextj] and board[nexti][nextj] == "O":
                            q.append((nexti, nextj))
                            visited[nexti][nextj] = 1
                        elif nexti < 0 or nexti > len(board) - 1 or nextj < 0 or nextj > len(board[0]) - 1:
                            yes = 0
                while yes and res:
                    marki, markj = res.pop()
                    board[marki][markj] = "X"
            
