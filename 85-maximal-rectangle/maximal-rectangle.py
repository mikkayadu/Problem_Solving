class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ROW , COL = len(matrix), len(matrix[0])
        for j in range(COL):
            matrix[0][j] = int(matrix[0][j])

        for i in range(ROW-1):
            for j in range(COL):
                
                matrix[i+1][j] = int(matrix[i][j]) + int(matrix[i+1][j]) if int(matrix[i+1][j]) else 0

        print(matrix)

        def largestRectangleArea( heights: List[int]) -> int:
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

        largest = 0
        for i in range(ROW):
            largest = max(largestRectangleArea(matrix[i]), largest)

        return largest
        