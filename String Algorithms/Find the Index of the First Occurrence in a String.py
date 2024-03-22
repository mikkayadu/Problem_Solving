class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k = len(needle); l  = 0
        cursum = ans = 0
        if len(needle) > len(haystack):
            return -1
        for i in range(k):
            cursum += (ord( haystack[i]) - ord("a") +1)*( 31**(k-i-1))
        for i in range(k):
            ans += (ord(needle[i]) - ord("a")+1) * (31 **(k-i-1))
        if cursum == ans:
            return 0
        
        for i in range(k, len(haystack)):
            cursum -= (ord(haystack[l]) - ord("a") +1)* (31 ** (k-1))
            cursum *= 31
            cursum += ord(haystack[i]) - ord("a") +1
            l+=1

            if cursum == ans:
                return l

        return -1

        
