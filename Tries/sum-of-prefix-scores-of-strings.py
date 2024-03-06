class TrieNode:
    def __init__(self):
        self.val = 0 
        self.children = {}

class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.val += 1 

    def collect(self, word: str) -> int:
        total = 0
        cur = self.root
        for char in word:
            if char in cur.children:
                cur = cur.children[char]
                total += cur.val
            
        return total

    def sumPrefixScores(self, words: list[str]) -> list[int]:
        for word in words:
            self.insert(word)  
        
        return [self.collect(word) for word in words]  


