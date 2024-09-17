class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj_list = defaultdict(list)
        count = defaultdict(int)
        queue = deque([])
        finish_time = [0] * (n + 1)
        

        for start, end in relations:
            adj_list[start].append(end)
            count[end] += 1
        
        for i in range(1, n+1):
            if count[i] == 0:
                queue.append(i)
                finish_time[i] = time[i-1]

        while queue:
            node = queue.popleft()
            for child in adj_list[node]:   
                finish_time[child] = max(finish_time[child], finish_time[node] + time[child-1])
                count[child] -= 1

                if count[child] == 0:
                    queue.append(child)


        return max(finish_time)
    
        
