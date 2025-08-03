class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxi = 0
        ans = ""
        for i in range(n):
            l, r = i, i

            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1; r += 1
            
            if r -l - 1 > maxi:
                ans = s[l+1: r]
                maxi = r-l-1

            l, r = i , i +1

            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1; r += 1
            
            if r -l - 1 > maxi:
                ans = s[l+1: r]
                maxi = r-l-1


        return ans
