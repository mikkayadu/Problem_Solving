class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        queue = deque()
        visit = set()
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0: queue.append((r, c))

        while  queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                
                for dr, dc in directions:
                    row = r + dr; col = c + dc
                    if min(row, col) < 0 or row == ROWS or col == COLS or (row,col) in visit:
                        continue
                    queue.append((row, col))
                    visit.add((row, col))
                    if mat[row][col] == 1:
                        mat[row][col] = mat[r][c] + 1
        return mat
                    


        
                    


        