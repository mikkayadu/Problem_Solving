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
        adj_list = {}

        for i in range(len(employees)):
            employee = employees[i]

            adj_list[employee.id] = [employee.subordinates, employee.importance]
        
        print(adj_list)
        ans = 0

        def dfs(i):
            nonlocal ans

            ans += adj_list[i][1]

            for child in adj_list[i][0]:
                dfs(child)
        dfs(id)
        return ans
            
        
        

        