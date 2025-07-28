class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        maxi = 0

        for r in range(len(heights)):
            cur = heights[r]

            while stack and heights[stack[-1]] > cur:
                top = stack.pop()
                right = (r - top) - 1
                sub = stack[-1] if stack else -1
                left = top - sub
                width = right + left
                print("width", width)
                area = heights[top] * width
                maxi = max(maxi, area)

            stack.append(r)
        

        return maxi
        