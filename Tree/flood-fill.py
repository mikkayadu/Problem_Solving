class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visit = set()
        initial_value = image[sr][sc]
        
        def dfs(r, c, visit, grid):
            ROWS, COLS = len(grid), len(grid[0])
            if min(r, c) < 0 or r == ROWS or c==COLS or (r, c) in visit or grid[r][c] != initial_value:
                return 
            
            visit.add((r, c))
            image[r][c] = color
            dfs(r, c+1, visit, grid)
            dfs(r, c-1, visit, grid)
            dfs(r+1, c, visit, grid)
            dfs(r-1, c, visit, grid)
        
        # for row in range(sr, len(image)):
        #     for col in range(sc, len(image[0])):
        #         if image[row][col] == initial_value and  (row, col) not in visit:
        #             dfs(row, col, visit, image)

        dfs(sr, sc, visit, image)
                

        return image
        
                    

        