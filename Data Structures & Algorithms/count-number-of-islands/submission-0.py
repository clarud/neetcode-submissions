class Solution:
    def dfs(self, coord):
        self.island_count += 1
        stack = []
        stack.append(coord)
        directions = [[0, 1], [0, -1], [1, 0], [-1 ,0]]
        while stack:
            x, y = stack.pop()
            self.visited[x][y] = True
            for direction in directions:
                nextrow, nextcol = direction[0] + x, direction[1] + y
                if (0 <= nextrow < self.num_row and 0 <= nextcol < self.num_col) and self.grid[nextrow][nextcol] == '1' and not self.visited[nextrow][nextcol]:
                    stack.append((nextrow, nextcol))

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.island_count = 0
        self.num_row = len(grid)
        self.num_col = len(grid[0])
        self.visited = [[False] * self.num_col for row in range(self.num_row)]
        for row in range(self.num_row):
            for col in range(self.num_col):
                if self.visited[row][col] or grid[row][col] == '0':
                    continue
                self.dfs((row, col))
        return self.island_count
                
