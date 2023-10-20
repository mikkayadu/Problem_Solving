class Solution:
    def check_maximum(self, mydict:dict):
        maximum = float('-inf')
        for index, value in mydict.items():
            maximum = max(maximum, value)
        return maximum

    def characterReplacement(self, s: str, k: int) -> int:
        mydict = {}; l=0
        longest = 0

        for r in range(len(s)):

            mydict[s[r]] = mydict.get(s[r], 0) + 1
            maximum = self.check_maximum(mydict)

            while  r-l+1 - maximum > k :
                mydict[s[l]] = mydict[s[l]] -1
                l+=1
            
            longest = max(longest, r-l+1)

        return longest


        
