class Solution:
    def longestPalindrome(self, s: str) -> int:
        mydict = Counter(s)
        count = 0

        if len(set(s)) ==1:
            return len(s)

        for key in mydict:
            if mydict[key]%2 == 0:
                count += mydict[key]
            elif mydict[key]%2 != 0:
                count += mydict[key]-1
        for values in mydict.values():
            if values%2!=0:
                count +=1
                break
        
        return count
