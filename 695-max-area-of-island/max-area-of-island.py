class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            if min(i,j) < 0 or i == ROW or j == COL or (i, j) in visited or grid[i][j] == 0: 
                return 0

            visited.add((i, j))
            maxi = 1

            for dx, dy in directions:
                maxi += dfs(i+dx, j+dy)
            
            return maxi

        ans = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1 and (i, j) not in visited:
                    ans = max(ans, dfs(i, j))
 

        return ans

            
        