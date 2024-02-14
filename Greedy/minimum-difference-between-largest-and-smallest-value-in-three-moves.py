class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 3:
            return 0

        #remove all small smallest
        first = nums[-1] - nums[3]
        #remove all largest
        second = nums[-4] - nums[0]
        #remove one small , two large
        third = nums[-3] - nums[1]
        #remove 2 small, one large
        fourth = nums[-2] - nums[2]
        return min(first, second, third, fourth)
        

        