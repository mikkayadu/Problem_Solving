# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         i = 0; n = len(nums)
#         while i< n:
#             if nums[i] < len(nums) and nums[i] != nums[nums[i]]:
#                 nums[i], nums[nums[i]] = nums[nums[i]], nums[i] An error might occur here because, nums[i] might be bigger on this line and since python
#evaluates the RHS first, youll get index out of bounds.
#             else:
#                 i+=1
#         print(nums)

        # return 1
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if 0<= nums[i] < n and nums[i] != nums[nums[i]]:
                nums[nums[i]], nums[i] =  nums[i], nums[nums[i]]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i:
                return i

        return n
