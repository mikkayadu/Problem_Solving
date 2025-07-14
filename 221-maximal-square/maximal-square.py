class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROW, COL = len(matrix) + 1, len(matrix[0]) + 1
        dp = [[0 for j in range(COL)] for i in range(ROW)]
        maxi = 0


        for i in range(1, ROW):
            for j in range(1, COL):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
                    maxi = max(maxi, dp[i][j])
        
        return maxi **2


    
        