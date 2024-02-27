class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        memo = {}

        def dp(pos, i):
            if i >= n :
                return 0

            if (pos, i) not in memo:
                #We are now coming to buy
                if pos == 0:
                    memo[(pos, i)] =  max(dp(1, i +1 ) - prices[i], dp(0, i + 1))
                
                #We've already bought, we need to sell
                else:
                    memo[(pos, i)] =  max(dp(0, i +1) + prices[i] - fee, dp(pos, i + 1) )
                
            return memo[(pos, i)]
            
        return dp(0, 0)
