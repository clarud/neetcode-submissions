class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        moves = [(0, 1),(0, -1),(1, 0),(-1 ,0)]
        queue = deque()
        max_depth = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 2:
                    continue
                queue.append((r, c, 0))
        while queue:
            i, j, m = queue.popleft()
            if grid[i][j] == 1:
                grid[i][j] = 2
                max_depth = max(m, max_depth)
            for move in moves:
                k, l = i + move[0], j + move[1] 
                if 0 <= k <= rows - 1 and 0 <= l <= cols - 1 and grid[k][l] == 1:
                    queue.append((k, l, m + 1))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return max_depth
                