class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visit  = set( deadends)  
        queue = deque(['0000']) if '0000' not in deadends else []
        length  = 0

        while queue:
            length += 1
            for i in range(len(queue)):
                node = list(queue.popleft())
                print()
                neighbours = []

                
                if "".join(node) == target:
                    return length-1

                for i in range(4):
                    before = node[i]
                    node[i] = str(int(node[i]) + 1) if node[i] != "9" else "0"
                    neighbours.append("".join(node))
                    node[i]  = before
                
                for i in range(4):
                    before = node[i]
                    node[i] = str(int(node[i]) - 1) if node[i] != "0" else "9"
                    neighbours.append("".join(node))
                    node[i]  = before
                
                for nei in neighbours:
                    if nei not in visit:
                        visit.add(nei)
                        queue.append(nei)
                
                
        return -1

        