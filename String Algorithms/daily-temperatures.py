class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for r in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[r]:
                i = stack.pop()
                ans[i] = r- i
            stack.append(r)
        return ans