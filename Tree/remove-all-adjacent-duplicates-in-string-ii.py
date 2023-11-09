class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        lst = list(s)
        stack = []

        for r in range(len(s)):
            if not stack or stack[-1][1] != s[r]:
                stack.append([1, s[r]])
            elif stack[-1][1] == s[r]:
                stack[-1][0] +=1
                
            if stack[-1][0] == k:
                stack.pop()
                
                
        ans = ""
        for num, letter in stack:
            ans+=letter*num
        return ans
            





        