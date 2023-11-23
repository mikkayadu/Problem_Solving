class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        
        def dfs(node,target, adjList, visit):
            if node == target:
                return True

            if node in visit:
                return            

            visit.add(node)
            
            for neighbour in adjList[node]:
                
                if dfs(neighbour, target, adjList, visit):
                    return True
            return False
            
        visit = set()
        adjList={}
        for src, dest in edges:
            if src not in adjList:
                adjList[src] = []
            if dest not in adjList:
                adjList[dest] = []
            adjList[src].append(dest)
            adjList[dest].append(src)

        

        return dfs(source, destination,adjList, visit)
            
            
        