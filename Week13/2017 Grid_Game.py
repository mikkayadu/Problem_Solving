class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        prefix = sum(grid[0])
        suffix = 0
        ans = float('inf')

        for i in range(len(grid[0])):
            prefix -= grid[0][i]
            diff = max(prefix, suffix)

            ans = min(ans, diff)

            suffix += grid[1][i]

        return ans
