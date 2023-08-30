class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0:1}
        res = 0
        curSum = 0

        for r in range(len(nums)):
            curSum += nums[r]
            diff = curSum -k 
            res += prefixSum.get(diff, 0)
            prefixSum[curSum] = prefixSum.get(curSum, 0) +1
        return res
