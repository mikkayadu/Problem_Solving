class Solution:
    def checkRecord(self, n: int) -> int:
        @lru_cache
        def dp(n, a, l):
            # 3 options 
            if l == 3:
                return 0
            if a == 2 :
                return 0
            if n  == 0:
                return 1
            return (dp(n-1, a, l+1) + dp(n-1, a , 0) + dp(n-1, a + 1, 0)) %( 10**9 + 7)
        return dp(n, 0, 0) % ((10**9) + 7)

        
