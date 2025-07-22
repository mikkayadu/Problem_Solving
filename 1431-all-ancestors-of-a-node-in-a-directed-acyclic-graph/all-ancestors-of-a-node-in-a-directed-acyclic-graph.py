class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """

        ans = [ set() for _ in range(n)]
        adj_list = defaultdict(list)
        edge_count = defaultdict(int)

        for start, end in edges:
            adj_list[start].append(end)
            edge_count[end] += 1

        start = []
        
        for i in range(n):
            if edge_count[i] == 0:
                start.append(i)

        queue = deque(start)

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()

                for nei in adj_list[node]:
                    ans[nei].add(node)

                    for val in ans[node]:
                        ans[nei].add(val)

                    edge_count[nei] -= 1

                    if edge_count[nei] == 0:
                        queue.append(nei)
        
        final_ans = []
        for lst in ans:
            if lst:
                final_ans.append(sorted(lst))
            else:
                final_ans.append([])
        return final_ans
                    



        