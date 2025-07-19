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



        for  i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in atlantic:
                    dfs(i, j , atlantic)
        
        for  i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in pacific:
                    dfs(i, j , pacific)
    
        return list(atlantic.intersection(pacific))


