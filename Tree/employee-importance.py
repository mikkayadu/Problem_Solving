"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mydict = {}
        for node in employees:
            mydict[node.id] = node
        
        
        def dfs(node, importance):
            
            
            if not node.subordinates:
                
                return node.importance
            

            for children in node.subordinates:
                importance += dfs(mydict[children], mydict[children].importance)
            return importance
        
        for node in employees:
            
            if node.id == id:
                return dfs(node, node.importance)

        

            

        