class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visit = set()
        def dfs(r, c, grid, visit):
            ROWS, COLS = len(grid), len(grid[0])
            if  min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == '0':
                return
            
            visit.add((r, c))
            dfs(r+1, c, grid, visit) #down
            dfs(r-1, c, grid, visit) #up
            dfs(r, c+1, grid, visit) #forward
            dfs(r, c-1, grid, visit) #back
                

        for row in range(len(grid)):
            for col  in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in visit:
                    dfs(row, col, grid, visit)
                    count +=1
        return count
        

                    
            
        