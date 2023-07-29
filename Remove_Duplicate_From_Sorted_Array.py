class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for r in range(len(nums)- 1):
            if nums[r] != nums[r+1]:
                l+=1
                nums[l] = nums[r+1]
        return l+1
