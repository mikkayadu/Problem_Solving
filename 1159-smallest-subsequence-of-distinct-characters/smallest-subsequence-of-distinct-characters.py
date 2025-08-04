class Solution:
    def smallestSubsequence(self, s: str) -> str:
        mydict = { n : i for i, n in enumerate(s)}

        stack = []

        for r in range(len(s)):
            cur  = s[r]
            if cur  in stack:
                continue

            while stack and stack[-1] > cur and mydict[stack[-1]] > r:
                stack.pop()
            
            
            stack.append(cur)
        
        return "".join(stack)


        
        