class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            queue = deque()
            grid[x][y] = "2"
            queue.append((x, y))
            while queue:
                currx, curry = queue.pop()
                for rowchange, colchange in pairwise((-1, 0, 1, 0, -1)):
                    nextx = currx + rowchange
                    nexty = curry + colchange
                    if nextx < 0 or nextx >= len(grid):
                        continue
                    if nexty < 0 or nexty >= len(grid[0]):
                        continue
                    if grid[nextx][nexty] == "1":
                        queue.append((nextx, nexty))
                        grid[nextx][nexty] = "2"
            return
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
        return count
