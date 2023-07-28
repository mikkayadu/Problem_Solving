class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans = ""
        nums = list(map(str, nums))

        nums.sort( reverse=True)
        print("sorted", nums)
        

        for i in range(len(nums)):
            for j in range(len(nums) -i -1):
                if int(nums[j] + nums[j+1]) < int(nums[j+1] + nums[j]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        print(nums)
        for num in nums:
            ans += num
        return str(int(ans))