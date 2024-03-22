class Solution:
    
    def minDistance(self, word1: str, word2: str) -> int:
        ans = 0
        n = len(word1)
        m = len(word2)
        memo = {}

        def dp(i, j):
            
            if i >= n :
                return m - j 
            
            if j >= m:
                return n -i
            
            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                return dp(i+1, j+1)

            memo[(i, j)] =  1 + min(
                dp(i+1, j +1), #replace
                dp(i, j+1), #insert
                dp(i+1, j)#delete
            )
            return memo[(i, j)]

        return dp(0, 0)
            
        
            
        