import bisect
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # for r in range(len(nums)):
        #     if nums[r] >= target:
        #         return r
        # return r+1

        return bisect.bisect_left(nums, target)
