class TrieNode:
    def __init__(self):

        self.is_end = False
        self.children = {}
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c  not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]

        cur.is_end = True

    def search(self, word: str, s=True) -> bool:
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False

        return cur.is_end if s else True
        

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, s=False)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)