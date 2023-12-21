class Solution:
    def racecar(self, target: int) -> int:
        
        queue = deque([(1,  1, 2)])
        length = 0
        visit = set()


        while queue:
            length += 1
            for i in range(len(queue)):
                node,  pos, speed = queue.popleft()

                if pos == target:
                    return length

                if (pos, speed) in visit or speed > 10000 or  speed < -10000:
                    continue
               
                visit.add((pos, speed))

                queue.append((node + 1, pos+speed, speed * 2))
                if speed >= 0:
                    queue.append((node + 1,pos, -1 ))
                else:
                    queue.append((node + 1, pos, 1))
            
        return length
            
            


        