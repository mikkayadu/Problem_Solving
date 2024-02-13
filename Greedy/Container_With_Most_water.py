class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) -1
        maxi = float("-inf")

        while l < r:
            maxi = max(maxi, (min(height[l] ,  height[r])  * (r -l)))

            if height[r] < height[l]:
                r-=1
            else:
                l +=1
        return maxi

        
