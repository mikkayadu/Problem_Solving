class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(target):
            if target == amount :
                return 0
            if target > amount:
                return float("inf")
            if target in memo:
                return memo[target]
            
            min_ = float("INF")
            for num in coins:
                min_ = min(min_, 1+ dp(target + num))
            memo[target] = min_
            return memo[target]
        ans = dp(0)
        return -1 if ans == float("inf") else  ans
            
            
            
            

        