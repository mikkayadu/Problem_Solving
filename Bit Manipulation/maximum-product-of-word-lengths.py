class Solution:
    def maxProduct(self, words: List[str]) -> int:
        alphabets = "abcdefghijklmnopqrstuvwxyz"; mydict = {}
        another = words.copy()

        for i, let in enumerate(alphabets):
            mydict[let] = i

        for i in range(len(words)):
            myarr = ['0'] * 26
            for let in words[i]: 
                myarr[mydict[let]] = '1'
            words[i] = "".join(myarr)
        

        maxi = 0
        for i in range(len(words)):
            for j in range(len(words)):
                if int(words[i], 2) & int(words[j], 2) == 0:
                    maxi = max(len(another[i]) * len(another[j]), maxi)
        return maxi


        