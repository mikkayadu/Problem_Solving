class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans = 0
        nums = set(nums)

        negatives = []
        for num in nums:
            if num < 0:
                negatives.append(num)
        if len(negatives) == len(nums):
            return max(negatives)


        for num in nums:
            if num > 0:
                ans += num
        
        return ans
        