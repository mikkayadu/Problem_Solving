class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        def djikstra(source):
            queue = [(0, source)]
            visited = set()
            
            while queue:
                
                for i in range(len(queue)):
                    old_cost, node = heappop(queue)
                    visited.add(node)
                    
                    if len(visited) == n:
                        return old_cost
                
                    for cost, nei in adj_list[node]:
                        if nei not in visited:
                            heappush(queue, (cost+old_cost, nei))
            return -1

        adj_list = defaultdict(list)
        for src, dest , cost in times:
            adj_list[src].append((cost, dest))
        

        
        
        ans = djikstra(k)
       
        return ans
