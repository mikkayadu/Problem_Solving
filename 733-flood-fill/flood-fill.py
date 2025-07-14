class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        prev_color = image[sr][sc]
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        visited = set()

        def dfs(i, j):
            print("call")
            visited.add((i, j))
            for dx, dy in directions:
                if not (min(i+dx, j+dy) < 0 or i+dx == n or j+dy == m or (i+dx, j+dy) in visited) and  image[i+dx][j +dy] == prev_color:
                    dfs(i +dx, j + dy)

        dfs(sr, sc)

        for i, j in visited:
            image[i][j] = color
        
        return image
            


                  