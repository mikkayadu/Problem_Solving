class UnionFind():
    def __init__(self, m, n):
        self.root = {}
        self.size = [[1 for i in range(n)] for _ in range(m)]
        print(self.size)
        for i in range(m):
            for j in range(n):
                self.root[(i, j)] = (i, j)
               



    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return  self.root[x]
    
    def union(self, x, y):
        rootX= self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.size[rootX[0]][rootX[1]] > self.size[rootY[0]][rootY[1]]:
                self.root[rootY] = rootX
                self.size[rootX[0]][rootX[1]] += self.size[rootX[0]][rootY[1]]
            else:
                self.root[rootX] = rootY
                self.size[rootY[0]][rootY[1]] += self.size[rootX[0]][rootX[1]]

class Solution:
    
    

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        ROW, COL = len(grid), len(grid[0])
        def check( i, j):
            if 0<=i<ROW and 0 <=j<COL:
                return True
            return False
        directions = [[1, 0], [1, -1], [0, 1], [0, -1]]
        
        mydict = {1:{'r':{3, 1}, 
                    'u':set(), 'd':set(), "l": {1, 4, 6}}, 
                2 : {'r':set(), 
                    'u':{2, 3, 4}, 'd':{5, 6}, "l": set()},
                3: {'r':set(), 
                    'u':set(), 'd':{2,5,6}, "l": {1,4, 6}}, 
                4:{'r':{3, 1}, 
                    'u':set(), 'd':{2,5,6}, "l": set()},
                5:{'r':set(), 
                    'u':{2,3,4}, 'd':set(), "l": {1, 4, 6}},
                6:{'r':set(), 
                    'u':{2,3,4}, 'd':set(), "l": {1, 4, 6}
                }}

        obj = UnionFind(ROW , COL)
        for i in range(ROW):
            for j in range(COL):
                num = grid[i][j] 

                #right
                if check(i, j+1) and grid[i][j + 1] in mydict[num]['r']:
                    obj.union((i, j), (i, j+1))
                #left
                if check(i, j-1) and grid[i][j -1] in mydict[num]['l']:
                    obj.union((i, j), (i, j-1))
                #up 
                if check(i-1, j) and grid[i-1][j] in mydict[num]['u']:
                    obj.union((i, j), (i-1, j))
                #down
                if check(i+1, j) and grid[i+1][j] in mydict[num]['d']:
                    obj.union((i, j), (i+1, j))
        
        return obj.find((0, 0)) == obj.find((ROW-1, COL-1))


        