class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = [0] * (len(nums) +1)
        
        for i in range(1, len(nums)+1):
            prefix[i] = prefix[i-1] + nums[i-1]
        return prefix[1:]
