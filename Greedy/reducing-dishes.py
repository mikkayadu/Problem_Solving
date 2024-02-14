class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        ans = 0
        n = len(satisfaction)
        neg = 0
        for i in range(n):
            if satisfaction[i] < 0:
                neg +=1 
        maxi = 0

        if neg == 0:
            for i, value in enumerate(satisfaction):
                maxi+= value * (i+1)
            return maxi

        for i in range(neg):
            ans = 0
            for j in range(i, n):
                ans += (j-i+1) * satisfaction[j]
            maxi = max(ans, maxi)

        
        return maxi
                
                
        