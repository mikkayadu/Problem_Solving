class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[float('inf') for _ in range(numCourses)] for _ in range(numCourses)]
        ans = []
        for src, dest in prerequisites :
            graph[src][dest] = 1
    
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        
        for src , dest in queries:
            if graph[src][dest] != float("inf"):
                ans.append(True)
            else:
                ans.append(False)
        return ans


        