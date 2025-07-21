class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic  = set(); pacific = set()
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0:
                    pacific.add((i, j))
                if j == 0:
                    pacific.add((i, j))

                if i == len(heights) - 1:
                    atlantic.add((i, j))
                
                if j == len(heights[0]) -1 :
                    atlantic.add((i, j))

        

        def dfs(i, j, visited):
            visited.add((i, j))
            for dx, dy in directions:
                nr, nc = i + dx, j + dy

                if (nr, nc) not in visited and min(nr, nc) >= 0 and nr < len(heights) and nc < len(heights[0])and heights[nr][nc] >= heights[i][j]:
                    
                    dfs(nr, nc, visited)



        for j in range(len(heights[0])):
            if (0, j ) in pacific:
                dfs(0, j, pacific)
        
        for j in range(len(heights)):
            if (j, 0) in pacific:
                dfs(j, 0, pacific)

        for j in range(len(heights[0])):
            if (len(heights) - 1, j ) in atlantic:
                dfs(len(heights) - 1, j, atlantic)
        
        for j in range(len(heights)):
            if (j, len(heights[0]) -1) in atlantic:
                dfs(j, len(heights[0]) -1, atlantic)
    
        return list(atlantic.intersection(pacific))


