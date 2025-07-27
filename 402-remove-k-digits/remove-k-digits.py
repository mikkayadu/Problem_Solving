class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        track = 0
        stack = []


        for  i in range(len(num)):
            cur = num[i]

            while stack and stack[-1] > cur and track < k:
                stack.pop()
                track += 1
            
            stack.append(cur)

        if track  < k:
            stack = stack[:len(stack) -(k - track) ]


        i = 0
       
        while i < len(stack):
            if stack[i] != "0":
                break
            i += 1

        ans = "".join(stack[i:]) if i < len(stack) else "0"
        return ans
        