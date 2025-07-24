class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        maxi = 0


        for r in range(len(heights)):
            cur = heights[r]
            while stack and heights[stack[-1]] > cur:
                top = stack.pop()
                height = heights[top]
                left = stack[-1] + 1 if stack else 0
                width = r -left
                area = height * width
                maxi = max(area, maxi)

            stack.append(r)

        return maxi



        