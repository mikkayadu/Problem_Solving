class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cursum = 0
        maxsum = float('inf')
        l = 0

        for r in range(len(nums)):
            cursum += nums[r]
            

            while cursum >= target:
                maxsum =min(maxsum, r-l+1)
                
                cursum -= nums[l]
                l+=1
            
            
        return maxsum if maxsum != float('inf') else 0