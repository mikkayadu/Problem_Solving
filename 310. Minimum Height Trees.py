class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        count = defaultdict(int)

        if n == 1:
            return [0]

        for src, dest in edges:
            adj_list[src].append(dest)
            adj_list[dest].append(src)
            count[src] += 1
            count[dest] += 1

        
        queue = []
        for i in range(n):
            if count[i] == 1:
                queue.append(i)
        
        queue = deque(queue)

        while queue:

            if n <= 2:
                return list(queue)

            for _ in range(len(queue)):
                node = queue.popleft()
                n -=1 
                for child in adj_list[node]:
                    count[child] -= 1

                    if count[child] == 1:
                        queue.append(child)
                







        
