class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        curmin = nums[0]

        for num in nums:
            while stack and num >= stack[-1][0]:
                stack.pop()

            if stack and num > stack[-1][1]:
                return True
            
            stack.append((num, curmin)) 
            curmin = min(curmin, num)
        return False
