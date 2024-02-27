class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        memo = {}
        def dp(r, c):
            if min(r, c) < 0  or c == COL : 
                return float("inf")
            if r == ROW  :
                return 0
            if (r, c) not in memo:
                memo[(r, c)] = matrix[r][c] + min(dp(r+1, c-1), dp(r +1, c) , dp(r + 1, c +1))
            return memo[(r, c)]
        
        return min([dp(0,j) for j in range(COL)])
            
        