class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

        

    def insert(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char in cur.children:
                cur = cur.children[char]

            else:
                cur.children[char] = TrieNode()
                cur = cur.children[char]

        cur.end_of_word = True

            

    def search(self, word: str) -> bool:
        cur = self.root

        for ch in word:
            if ch in cur.children:
                cur = cur.children[ch]
            else:
                return False
        
        return cur.end_of_word



    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            if ch in cur.children:
                cur = cur.children[ch]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)