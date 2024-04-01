class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        s = s[::-1]
        h_hash = 0
        
       
        def val(c):
            return ord(c)-ord("a") + 1

        p = 1
        for j in range(k-1):
            h_hash = (h_hash * power) % modulo
            h_hash = (h_hash + val(s[j])) % modulo
            p = (p * power) % modulo


        for i in range(k-1, len(s)):
            h_hash = (h_hash * power) % modulo
            h_hash = (h_hash + val(s[i])) % modulo

            if h_hash == hashValue:
                ans = s[i-k+1:i+1][::-1]
            
            
            h_hash = (h_hash - p * val(s[i-k+1])) % modulo
        
        return ans
        
        
        