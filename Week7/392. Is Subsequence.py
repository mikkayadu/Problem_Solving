class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, 0

        while r <len(t) and len(s) > 0 and len(t) > 0:
            if t[r] == s[l]:
                l += 1
            r+=1

            if l==len(s):
                break
        
        return True if l == len(s) else False
