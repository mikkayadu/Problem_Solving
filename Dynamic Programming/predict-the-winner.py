class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}
        def dp(s, e):
            if s == e:
                return nums[s]
            if (s, e) not in memo:
                memo[(s, e)] = max(nums[s] - dp(s+1, e) , nums[e] - dp(s, e-1))
            return memo[(s, e)]
        
        ans = dp(0, n -1)
        return True if ans>=0 else False

        