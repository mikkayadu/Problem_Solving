class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: abs(x[1] - x[0]), reverse=True)
        ans = 0
        
        a_count = 0; b_count = 0
        
        for i in range(len(costs)):
            if b_count== len(costs)//2 or (costs[i][1] > costs[i][0] and a_count< len(costs)//2):
                a_count +=1
                ans += costs[i][0]
            else:
                b_count +=1
                ans += costs[i][1]
        
        
        return ans
    

       

        
