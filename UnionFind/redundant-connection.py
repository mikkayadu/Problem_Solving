class UnionFind():
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.size = [1 for i in range(size)]

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return  self.root[x]
    
    def union(self, x, y):
        rootX= self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]
        else:
            return [x+1, y+1]
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        obj = UnionFind(len(edges))
        ans = ""
        for src , dest in edges:
            var = obj.union(src-1, dest-1)
            if var != None:
                ans = var
        return ans
        
        
        