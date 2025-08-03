class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mydict = defaultdict(int)
        l = 0
        maxi = 0

        for r in range(len(s)):
            mydict[s[r]] += 1

            while mydict[s[r]] > 1:
                mydict[s[l]] -= 1
                l += 1 

            maxi = max(maxi, r - l + 1)
        

        return maxi

        