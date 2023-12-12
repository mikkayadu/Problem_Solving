class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for i, lst in enumerate(rooms):
            adj_list[i] = lst
        
        queue = deque([0])
        visit = set([0])

        def bfs(adj_list):
            
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    for neighbour in adj_list[node]:
                        if neighbour not in visit:
                            visit.add(neighbour)
                            queue.append(neighbour)
            

        bfs(adj_list)
        return True if len(visit) == len(rooms) else False
        