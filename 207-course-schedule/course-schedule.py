class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = defaultdict(list)
        edgecount = defaultdict(int)
        visited = set()
        queue = deque([])

        for start, end in prerequisites:
            adjlist[end].append(start)
            edgecount[start] += 1

        
        for i in range(numCourses):
            if edgecount[i] == 0:
                queue.append(i)
        
        print("edge_count", edgecount)
        print("adj_list", adjlist)

        ans = len(queue)
        while queue:
            node = queue.popleft()
            visited.add(node)

            for nei in adjlist[node]:
                edgecount[nei] -= 1

                if edgecount[nei] == 0:
                    if nei not in visited:
                        queue.append(nei)
                        ans += 1
        
        return ans == numCourses

        

        