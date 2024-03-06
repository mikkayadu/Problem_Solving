class TrieNode:
    def __init__(self):

        self.word = None
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

        cur.word = word

        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROW, COL = len(board), len(board[0])
        direction  = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        solutions  = []

        obj = Trie()
        for word in words:
            obj.insert(word)
            

        def check(i, j):
            if 0 <= i < ROW and 0 <=j<COL:
                return True
            return False
        
        def backtrack(i, j, cur):
            if not  check(i, j) or board[i][j] not in cur.children:
                return 
            
            original = board[i][j]
            cur  = cur.children[original]
            board[i][j] = "#"

            if cur.word != None:
                solutions.append(cur.word)
                cur.word = None
            
            for dr, dc in direction:
                backtrack(i + dr, j + dc, cur)
            board[i][j] = original

        
        for row in range(ROW):
            for col in range(COL):
                backtrack(row, col, obj.root)

        return solutions
            


        