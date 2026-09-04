from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        g_rows = len(grid)
        g_cols = len(grid[0])
        queue = deque()
        max_length = 0
        moves = [(0, 1),(0, -1),(1, 0),(-1, 0)]
        for i in range(g_rows):
            for j in range(g_cols):
                if grid[i][j] == 1:
                    length = 0
                    queue.append((i, j))
                    while queue:
                        currx, curry = queue.popleft()
                        length += 1
                        max_length = max(max_length, length)
                        grid[currx][curry] = 0
                        for x, y in moves:
                            nextx = currx + x
                            nexty = curry + y
                            if 0 <= nextx <= g_rows - 1 and 0 <= nexty <= g_cols - 1 and grid[nextx][nexty] == 1:
                                grid[nextx][nexty] = 0
                                queue.append((nextx, nexty))
        return max_length