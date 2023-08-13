class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxSeq = 1
        l = 0
        curr = 1

        if len(nums) ==0:
            return 0
        if len(nums) == 1:
            return 1
        nums =  sorted(list(set(nums)))


       
        for r in range(len(nums)-1):
            if nums[r+1]-nums[r] == 1:
                curr += 1
                maxSeq = max(curr, maxSeq)
            else:
                curr =1
                
        return maxSeq
