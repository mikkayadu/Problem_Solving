class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.size = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
       
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        obj = UnionFind(26)
        for item in equations:
            operator = item[1:-1]
            
            if operator == "==":
                obj.union(ord(item[0]) - ord('a'), ord(item[-1]) - ord('a'))

        for item in equations:
            operator = item[1:-1]
            if operator == "!=":
                ans = obj.find(ord(item[0]) - ord('a')) == obj.find(ord(item[-1]) - ord('a'))
                if ans == True:
                    return False


        return True