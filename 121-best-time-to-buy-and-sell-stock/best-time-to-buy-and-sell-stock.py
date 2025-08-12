class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = float("inf")
        maxi = 0

        for i in range(len(prices)):
            min_so_far = min(min_so_far, prices[i])
            maxi = max(maxi, prices[i] - min_so_far)
        

        return maxi
        