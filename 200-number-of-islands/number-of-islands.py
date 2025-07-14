class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        visited = set()

        def dfs(i, j):
            if min(i, j) < 0 or i == ROW or j == COL or (i, j) in visited or grid[i][j] == "0":
                return 
            visited.add((i, j))
            for dx, dy in directions:
                dfs(i + dx, j + dy)
                

        ans = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    ans += 1
        
        return ans


        