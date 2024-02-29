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
    
    def longestWord(self, words: List[str]) -> str:
        n = len(words)
        root = self.root
        for word in words:
            self.addWord(word)
        
        
        ans = ""

        def helper(root, prefix):
            nonlocal ans
            if root != self.root:
                if root.is_end == False:
                    prefix = prefix[:-1]
                    
                if not root.children or root.is_end == False:
                    if len(prefix) > len(ans):
                        ans = prefix
                    return

            for letter in sorted(list(root.children.keys())):
                helper(root.children[letter], prefix + letter)

            return ans
                    

        return helper(self.root,"")
        