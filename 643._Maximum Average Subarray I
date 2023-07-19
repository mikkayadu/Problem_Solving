class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cursum = sum(nums[:k])
        max_sum = cursum/k

        for r in range(k, len(nums)):
            cursum += nums[r]
            l = r -k 
            cursum -= nums[l]

            max_sum = max(max_sum,cursum/k)
        return max_sum

