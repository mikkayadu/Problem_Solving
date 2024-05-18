class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        ROW = len(board); COL = len(board[0])
        def check(row, col, num):
            if num in board[row] :
                return False
            
            column = set()
            
            for r in range(len(board)):
                column.add(board[r][col])
            
            if num in column :
                return False
            
            grid_row = row//3 * 3
            grid_col = col//3 * 3

            for  i in range(grid_row , grid_row + 3):
                for j in range(grid_col , grid_col + 3):
                    if board[i][j] == num :
                        return False
            return True

        def solve(r, c):
            if r == ROW :
                return True
            if c == COL :
                return solve(r+1, 0)
            
            if board[r][c] == ".":
                for i in range(0, 9):
                    if check(r, c, str(i+1) ):
                        board[r][c] = str(i+1)
                        if solve(r, c+1):
                            return True
                    
                        board[r][c] = "."
            else:
                return solve(r, c+1)
        solve(0, 0)
    
