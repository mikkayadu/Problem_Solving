class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list  = defaultdict(list)
        visited = set()

        for src, dest in edges:
            adj_list[src].append(dest)
            adj_list[dest].append(src)
        
        print(adj_list)

        def dfs(node):
            if node == destination:
                return True

            visited.add(node)

            for child in adj_list[node]:
                if child not in visited:
                    if dfs(child) == True:
                        return True
            
            return False
        
        return dfs(source)
            
            
        