class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        edge_count = defaultdict(int)
        ans = []

        for i in range(len(graph)):
            if graph[i]:
                for values in graph[i]:
                    adj_list[values].append(i)
                    edge_count[i] += 1
            else:
                adj_list[i]

        for i in range(len(graph)):
            if edge_count[i] == 0:
                ans.append(i)

        queue = deque(ans)
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()

                for nei in adj_list[node]:
                    edge_count[nei] -= 1
                    if edge_count[nei] == 0:
                        queue.append(nei)
                        ans.append(nei)
        return sorted(ans)


            



            

        return [1]
       

        
        
        
       
        
        

        

                

        
        