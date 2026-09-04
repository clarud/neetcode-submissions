class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row = len(grid)
        col = len(grid[0])
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        q = deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c] != 0:
                    continue
                q.append((r,c))
                while q:
                    r, c = q.popleft()
                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        # Only move to valid land cells where we can improve distance
                        if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] > grid[r][c] + 1:
                            grid[nr][nc] = grid[r][c] + 1
                            q.append((nr, nc))
                