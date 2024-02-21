class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i, target):
            if i ==len(nums): 
                return 1 if target == 0 else 0
            
            if (i, target) in memo:
                return memo[(i, target)]
            
            memo[(i, target)] = dp(i+1 , target - (-1 * nums[i])) + dp(i+1, target - (1 * nums[i]))
            return memo[(i, target)]
            

        return dp(0, target)