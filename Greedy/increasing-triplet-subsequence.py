class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i, j = float('inf'), float('inf')

        for r in range(len(nums)):
            if nums[r] <= i:
                i = nums[r]
            elif  nums[r] <=j :
                j = nums[r]
            else:
                return True
        
        return False
            