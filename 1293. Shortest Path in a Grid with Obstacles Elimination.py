class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid), len(grid[0])
        def outbound(i, j):
            if min(i, j) < 0 or i == m or j == n :
                return True
            return False

        if grid[0][0] and k == 0:
            return 0

        queue = deque([(0, 0,k)])
        ans = 0
        visited = set()
        while queue:
            for i in range(len(queue)):
                r, c,k = queue.popleft()

                if r == m -1 and c == n -1 : return ans 

                if not outbound(r+1, c):
                    if grid[r+1][c] == 0 and (r+1, c, k) not in visited:
                        queue.append((r+1, c,k))
                        visited.add((r+1, c,k))

                    if grid[r+1][c] == 1 and k>=1 and (r+1, c, k-1) not in visited:
                        queue.append((r+1, c,k-1))
                        visited.add((r+1, c,k-1))
                    
                
                
                if not outbound(r, c+1):
                    if grid[r][c+1] == 0 and (r, c+1,k) not in visited:
                        queue.append((r, c+1, k))
                        visited.add((r, c+1, k))

                    if grid[r][c+1] == 1 and k>=1 and (r, c+1,k-1) not in visited:
                        queue.append((r, c+1,k-1))
                        visited.add((r, c+1, k-1))

                if not outbound(r-1, c):
                    if grid[r-1][c] == 0 and (r-1, c, k) not in visited:
                        queue.append((r-1, c, k))
                        visited.add((r-1, c, k))

                    if grid[r-1][c] == 1 and k>=1 and (r-1, c, k-1) not in visited:
                        queue.append((r-1, c,k-1 ))
                        visited.add((r-1, c, k-1))
                
                if not outbound(r, c-1):
                    if grid[r][c-1] == 0 and (r, c-1, k) not in visited:
                        queue.append((r, c-1, k))
                        visited.add((r, c-1, k))


                    if grid[r][c-1] == 1 and k>=1 and (r, c-1, k-1) not in visited:
                        queue.append((r, c-1,k-1 ))
                        visited.add((r, c-1, k-1))
                
            ans += 1
            
        return -1
                    

        
