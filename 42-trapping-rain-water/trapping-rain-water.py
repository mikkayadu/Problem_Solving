class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_value = height[n-1]
        max_index = n -1 
        mydict = {n-1: (height[n-1], n-1)}
        stack = []

        if n == 1:
            return 0

        for i in range(n):
            while stack and stack[-1][1] <= height[i]:
                index, value = stack.pop()
                mydict[index] =(height[i], i)

            stack.append((i, height[i]))
        
        if stack:
            for i in range(len(stack) -1):
                index, value = stack[i]
                mydict[index] = (stack[i+1][1], stack[i+1][0])
        

        i = 0
        ans  = 0
        while i < n-1:
            if height[i] == 0:
                i +=1
                continue
            end = mydict[i][1]
            ans += (min(height[i], height[end]) * ( end - i -1)) - sum(height[i+1:end])
            i = end
            
        return ans
        

        