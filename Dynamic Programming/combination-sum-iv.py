class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo  = {}
        def dp(target):
            if target == 0:
                return 1
            if target< 0:
                return 0
            
            if target not in memo:
            
                add = 0
                for num in nums:
                    add += dp(target - num) 

                memo[target] = add
            return memo[target]
        return dp( target)
