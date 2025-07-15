class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            if (i, j) in visited:
                return 0

            if min(i, j) < 0   or i == ROW or j == COL or grid[i][j] == 0:
                return 1
                
            visited.add((i, j))
            ans = 0

            for dx, dy in directions:
                row, col = i + dx, j + dy
                ans += dfs(row, col)
            
            return ans 

        
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    return dfs(i,j)
            


        