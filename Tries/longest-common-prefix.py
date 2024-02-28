class TrieNode:
    def __init__(self):

        self.is_end = False
        self.children = {}



    

class Solution:
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c  not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]

        cur.is_end = True

    def search(self, word: str, s=True) :
        cur = self.root
        

        for i in range(len(word)):
            if word[i] in cur.children:
                if len(cur.children) > 1:
                    return word[:i]
                cur = cur.children[word[i]]
        return word
                
    

    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = min(strs, key=len)
        if word =="":
            return ""
        for w in strs:
            self.insert(w)
        return self.search(word, True)

        

        