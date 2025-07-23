class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0] * n


        for r in range(n):
            temp = temperatures[r]

            while stack and temperatures[stack[-1]]  < temp:
                idx = stack.pop() 
                ans[idx] = r - idx


            stack.append(r)
        
        return ans

        