class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        def dp(i, memo:dict):
            if i>= len(nums):
                return 0
            if i not in memo:
                memo[i] = max(nums[i] + dp(i+2, memo), dp(i+1, memo))
            return memo[i]
        
        ans1 = dp(1, {})
        nums = nums[:-1]
        ans2 = dp(0, {})
        return max(ans1, ans2)


        