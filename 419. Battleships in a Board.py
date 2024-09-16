class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        visited = set()
        n, m = len(board), len(board[0])
        def dfs(i, j):
            if i == n or j == m or board[i][j] == ".":
                return 0
            visited.add((i+1, j))
            visited.add((i, j + 1))
            dfs(i+1, j)
            dfs(i, j+1)

        ans = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == "X" and (i, j) not in visited:
                    dfs(i, j)
                    ans += 1
        return ans
                


            
        return dfs(0,0)
