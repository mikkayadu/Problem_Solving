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




class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        obj = UnionFind(n)


        for src, dest in edges:
            obj.union(src, dest)
        
        return obj.find(source) == obj.find(destination)
            
        