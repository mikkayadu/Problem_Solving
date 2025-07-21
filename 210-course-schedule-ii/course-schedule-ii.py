class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        adj_list = defaultdict(list)
        edge_count = defaultdict(int)
        ans = []


        for end, start in prerequisites:
            adj_list[start].append(end)
            edge_count[end] += 1
        
        for i in range(numCourses):
            if edge_count[i] == 0:
                ans.append(i)
        
        queue = deque(ans)


        while queue:
            for i in range(len(queue)):
                node = queue.popleft()

                for nei in adj_list[node]:
                    edge_count[nei] -= 1

                    if edge_count[nei] == 0:
                        ans.append(nei)
                        queue.append(nei)
        
        return ans if len(ans) == numCourses else []




        