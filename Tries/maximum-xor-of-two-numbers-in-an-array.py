class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end = True

    def search(self, word):
        cur  = self.root
        ans = ""
        for c in word:
            
            if c == "0": 
                c = "1"
            else:
                c = "0"

            if c in cur.children:
                cur = cur.children[c]
                ans += c
            else:
                if c == "1":
                    cur = cur.children["0"] 
                    ans += "0"
                else:
                    cur = cur.children["1"]
                    ans += "1"
        
        return int(ans, 2) ^ int(word, 2)
            
            
    def findMaximumXOR(self, nums: List[int]) -> int:
        bit_length = max(nums).bit_length()
        nums = [bin(num)[2:].zfill(bit_length) for num in nums]
        maxi = float("-inf")

        
        for num in nums:
            self.addWord(num)
        
        for num in nums:
            
            maxi = max(self.search(num), maxi)
        
        return maxi
        
