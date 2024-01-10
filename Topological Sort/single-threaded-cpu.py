class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort()

        res, heap = [], []
        i, time = 0, tasks[0][0]

        while heap or i<len(tasks):
            while i<len(tasks) and time >= tasks[i][0]:
                heappush(heap, [tasks[i][1], tasks[i][2]])
                i+=1
        
            if not heap:
                time = tasks[i][0]
            else:
                ptime, index = heappop(heap)
                time += ptime
                res.append(index)
        return res

        
            
        