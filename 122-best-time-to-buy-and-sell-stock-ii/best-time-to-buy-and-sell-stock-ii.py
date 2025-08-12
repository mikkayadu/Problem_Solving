class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = float("inf")
        ans = 0

        for i in range(len(prices)):
            min_so_far = min(min_so_far, prices[i])

            if prices[i] > min_so_far:
                ans += prices[i]  - min_so_far
                min_so_far = prices[i]
            
        return ans
        