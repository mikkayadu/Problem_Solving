class UnionFind:
    def __init__(self, string):
        self.root = {string[i]:string[i] for i in range(len(string))}
        print(self.root)

    def find(self, x):
        if x not in self.root:
            return x
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
       
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
        #     if self.size[rootX] > self.size[rootY]:
        #         self.root[rootY] = rootX
        #         self.size[rootX] += self.size[rootY]
        #     else:
            if rootX < rootY:
                self.root[rootY] = rootX
                    # self.size[rootY] += self.size[rootX]
            else:
                self.root[rootX] = rootY

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        obj = UnionFind(s1+s2)
        a = []
        for i in range(len(s1)):
            a.append([s1[i], s2[i]])
        
        for src, dest in a:
            obj.union(src, dest)
        
        ans = ""
        for letter in baseStr:
            ans += obj.find(letter)

        return ans



        