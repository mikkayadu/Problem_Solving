class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [[]  for _ in range(n)]
        
        queue = deque([])
        edge_count = defaultdict(int)
        adj_list = defaultdict(list)

        for src, dest in edges:
            adj_list[src].append(dest)
            edge_count[dest] +=1
      

        for i in range(n):
            if edge_count[i] == 0:
                queue.append(i)
        
        
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                

                for  nei in adj_list[node]:
                    for val in ans[node]:
                        if val not in ans[nei]:
                            ans[nei].append(val)
                    ans[nei].append(node)
                   
                    
                    edge_count[nei] -= 1

                    if edge_count[nei] == 0:
                        queue.append(nei)
        
        ans = list(map(sorted, ans))
        return ans


        