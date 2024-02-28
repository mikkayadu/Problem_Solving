class TrieNode():
    def __init__(self):
        self.is_end = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
       
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur= cur.children[c]
        cur.is_end = True

     
    def search(self, word):
        n = len(word)
        cur = self.root
        def dfs(curr, i):

            if i == n:
                return curr.is_end

            if word[i] != ".":
                if word[i] in curr.children:
                    return dfs(curr.children[word[i]], i+1)
                    
                else:
                    return False

            else:
                for child in curr.children.values():
                    if dfs(child, i+1):
                        return True
                    
            return False
        return dfs(cur, 0)

                    
        
        
       

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)