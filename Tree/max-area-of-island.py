class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maximum = 0
        visit = set()
        def dfs(r, c , grid, visit):
            ROW, COL = len(grid), len(grid[0])
            count = 0
            if min(r,c) < 0  or r == ROW or c == COL or (r, c) in visit or grid[r][c] == 0:
                return 0
            
            count +=1
            visit.add((r,c))
            

            count += dfs(r, c+1, grid, visit) 
            count += dfs(r, c-1, grid, visit)
            count += dfs(r+1, c, grid, visit)
            count += dfs(r-1, c, grid, visit)
            return count
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visit:
                    mycount = dfs(row, col, grid,visit)
                    print(mycount)
                    maximum = max(mycount, maximum)
        return maximum
            

            
        