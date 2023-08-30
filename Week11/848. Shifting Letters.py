class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        alphabets = list("abcdefghijklmnopqrstuvwxyz")
        mydict = {}
        for index, value in enumerate(alphabets):
            mydict[value] = index
        s = list(s)
        n = len(s) 

        
        prefix = [0] * (n+1)
        prefix[n] = 0
        for i in range(len(prefix)-1, 0, -1):
            prefix[i-1] = prefix[i] + shifts[i-1]
        print(prefix)

        for r in range(len(shifts)):
            s[r] = alphabets[(mydict[s[r]]+prefix[r])%26]
        return "".join(s)
