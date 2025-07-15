class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        ROW, COL = len(grid), len(grid[0])
        visited = set()

        mydict= {1 : {(0, -1) : [1,4,6], (0, 1): [1,3,5], (-1, 0) : [], (1, 0) : []},
        2 : {(0, -1) : [], (0, 1): [], (-1, 0) : [2,3,4], (1, 0) : [2,5,6]}, 
        3 : {(0, -1) : [1,4,6], (0, 1): [], (-1, 0) : [], (1, 0) : [2,5,6]},
        4 : {(0, -1) : [], (0, 1): [1,3,5], (-1, 0) : [], (1, 0) : [2,5,6]},
        5:  {(0, -1) : [1,4,6], (0, 1): [], (-1, 0) : [2,3,4], (1, 0) : []},
        6:  {(0, -1) : [], (0, 1): [1,3,5], (-1, 0) : [2,3,4], (1, 0) : []}
        }

        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]


        def dfs(i, j):
            if i == ROW -1 and j == COL - 1:
                return True
            
            

            for dx , dy in directions :
                new_row , new_col  = i + dx, j  + dy
                if not (min(new_row, new_col) < 0 or new_row == ROW or new_col == COL or (new_row, new_col) in visited): 

                    visited.add((i, j))
                    new_street = grid[new_row][new_col]
                    print("new_street", new_street)

                    if new_street in  mydict[grid[i][j]][(dx,dy)]:
                        if dfs(new_row, new_col):
                            return True
            
            return False
        
        return dfs(0, 0)

        