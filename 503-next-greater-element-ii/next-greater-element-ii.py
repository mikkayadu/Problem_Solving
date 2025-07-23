class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        nums = nums + nums
        n = len(nums)
        ans = [-1] * n 

        for r in range(n):
            cur = nums[r]

            while stack and nums[stack[-1]] < cur:
                idx = stack.pop()
                ans[idx] = cur

            stack.append(r)
            

        return ans[:n//2]


        