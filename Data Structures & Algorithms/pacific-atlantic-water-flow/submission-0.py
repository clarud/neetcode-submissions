class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rownum = len(heights) 
        colnum = len(heights[0])
        pac = [[0] * colnum for _ in range(rownum)]
        atl = [[0] * colnum for _ in range(rownum)]
        for row in range(rownum):
            for col in range(colnum):
                if row == 0 or col == 0:
                    pac[row][col] = 1
                if row == rownum - 1 or col == colnum - 1:
                    atl[row][col] = 1
        directions = [(1, 0),(-1 ,0 ),(0, 1),(0, -1)]
        q = deque()
        res = []
        for row in range(rownum):
            for col in range(colnum):
                vis = [[0] * colnum for _ in range(rownum)]
                if pac[row][col] != 1 and atl[row][col] != 1:
                    continue
                q.append((row, col))
                while q:
                    currrow, currcol = q.popleft()
                    if pac[row][col]:
                        pac[currrow][currcol] = 1
                    if atl[row][col]:
                        atl[currrow][currcol] = 1
                    vis[currrow][currcol] = 1
                    for move in directions:
                        newrow, newcol = currrow + move[0], currcol + move[1]
                        if 0 <= newrow <= rownum - 1 and 0 <= newcol <= colnum - 1 and heights[newrow][newcol] >= heights[currrow][currcol] and vis[newrow][newcol] == 0:
                            q.append((newrow, newcol))
        return [[row, col] for row in range(rownum) for col in range(colnum) if atl[row][col] and pac[row][col]]




