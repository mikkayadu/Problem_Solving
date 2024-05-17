class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        stack = []
        MOD = 10** 9 +7

        for i, n in enumerate(arr):
            while stack and n<stack[-1][1]:
                j, m = stack.pop()
                left = j - stack[-1][0] if stack  else j+1
                right = i - j
                res = (res + left * right * m)%MOD
            stack.append((i, n))

        for i in range(len(stack)):
            j, m = stack[i]
            left = j - stack[i-1][0] if i-1>=0 else j+1
            right = len(arr) -j 
            res = ((res + left * right * m)%MOD)

        return res
        
