class UnionFind:
    def __init__(self,accounts):
            set_ = set()
            for row in accounts:
                for col in row[1:]:
                    set_.add((col))


            self.root = {i:i for i in set_}
            
            

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            
                self.root[rootY] = rootX


    def printout(self):
        emailGroups = defaultdict(set)
        for email in self.root:
            root = self.find(email)  
            emailGroups[root].add(email)
        return emailGroups
       
        

        

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mydict = {}
        ans = []

        for row in accounts:
            for email in row[1:]:
                mydict[email] = row[0]
        print("mydict", mydict)

        obj = UnionFind(accounts)

        for row in accounts:
            row = row[1:]
            for i in range(len(row) -1):
                obj.union(row[i], row[i+1])

        print("obj.root",obj.root)

        for key, value in obj.printout().items():
            mylist = []
            mylist.append(mydict[key])
            for email in sorted(value):
                mylist.append(email)
            ans.append(mylist)
        return ans

        