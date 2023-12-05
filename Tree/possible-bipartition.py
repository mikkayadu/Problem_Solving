class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(node, dislikes):
            for neighbour in dislikes[node]:
                if color[neighbour] == -1:
                    if color[node] == 0:
                        color[neighbour] = 1
                    else:
                        color[neighbour] = 0
                    if not dfs(neighbour, dislikes):
                        return False
                else:
                    if color[node] ==  color[neighbour]:
                        return False
            return True


        
        color = [0] + [-1 for _ in range(n)]
        adj_list = defaultdict(list)
        for key, value in dislikes:
            adj_list[key].append(value)
            adj_list[value].append(key)

        for node in adj_list:
            if color[node] == -1:
                color[node] = 0
                if not dfs(node, adj_list):
                    return False
        return True
        






        
        