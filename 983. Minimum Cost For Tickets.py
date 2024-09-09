class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day = 0
        n = len(days)
        memo = {}

        def dp(i, day):
            if i == n:
                return 0
            if (i, day ) in memo:
                return memo[i, day]

            if day < days[i]:
                first = costs[0] + dp(i+1, days[i])
                
                second = costs[1] + dp(i+1, days[i] + 6)
                third = costs[2] + dp(i+1, days[i] + 29)

                memo[i, day] =  min(first, second, third)
                return memo[i, day]
            else:
                memo[i, day] =  dp(i+1, day)
                return memo[i, day]
        return dp(0, 0)

            

            
                


        
        
