class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = {}
        def dp(i):
            if i == 0:
                return 0
            if i == 1:
                return 1
                
            if i in memo:
                return memo[i]
            if i %2 == 0:
                memo[i] = dp(i//2)
            else:
                memo[i] = dp(i//2) + dp((i//2) + 1)
            memo[i-1] = dp(i-1)

            return memo[i]
        dp(n)
        print("memo", memo)
        return max(memo.values()) if memo else n

            
        