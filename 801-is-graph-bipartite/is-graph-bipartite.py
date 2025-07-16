class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        def dfs(node):
            temp = True
            for nei in graph[node]:
                if color[nei] == -1:
                    if color[node] == 0:
                        color[nei] = 1
                    else:
                        color[nei] = 0
                    
                    temp = temp and dfs(nei)
                elif color[nei] == color[node]:
                    return False

            
            
            return temp
            

        result = True
        for node in range(n):
            if color[node] == -1:
                color[node] = 0
                result = result and dfs(node)
        

        return result


        