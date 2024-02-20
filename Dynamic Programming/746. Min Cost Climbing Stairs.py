class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        memo = {}
        def dp(i):
           
            if i == 0:
                return cost[i]
            if i ==1 :
                return cost[i]
            if i in memo:
                return memo[i]
            memo[i] = cost[i] + min(dp(i-1) , dp(i-2))
            return memo[i]
        return dp(len(cost) -1)
