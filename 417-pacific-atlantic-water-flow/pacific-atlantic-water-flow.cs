public class Solution {

    private int[][] heights;
    private int ROW;
    private int COL;

    private List<(int, int)> directions = new List<(int, int)>
    {
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    };

    public IList<IList<int>> PacificAtlantic(int[][] heights) {
        this.heights = heights;
        ROW = heights.Length;
        COL = heights[0].Length;
        HashSet<(int, int)> pacific = new HashSet<(int, int)> ();
        HashSet<(int, int)> atlantic = new HashSet<(int, int)> ();
        
        


        for (int i = 0; i < ROW; i ++){
            for (int j = 0; j < COL; j++)
            {
                if (i == 0)
                    pacific.Add((i, j));

                if (j == 0)
                    pacific.Add((i, j));
                
                if (j == COL - 1)
                    atlantic.Add((i,j));

                if (i == ROW-1)
                    atlantic.Add((i, j));
            }
        }

        for (int i = 0; i < COL; i ++){
            Dfs(0, i, pacific);
        }

        for (int i=0; i < ROW; i++)
        {
            Dfs(i, 0, pacific);
        }

        for (int i=0; i < COL; i++){
            Dfs(ROW-1, i, atlantic);
        }

        for (int i =0; i < ROW; i++){
            Dfs(i, COL-1, atlantic);
        }

        var result = new List<IList<int>>();
        foreach (var cell in pacific.Intersect(atlantic))
        {
            result.Add(new List<int> { cell.Item1, cell.Item2 });
        }

        return result;

        
    }

    public void Dfs(int r, int j, HashSet<(int, int)> visited)
    {
        visited.Add((r, j));

        for (int i = 0; i < directions.Count; i ++){
            var (dx, dy) = directions[i];

            int nr = r + dx; int ny = j + dy; 

            if (!visited.Contains((nr, ny)) && Math.Min(nr, ny) >= 0 && nr <= ROW - 1 && ny <= COL - 1 && heights[nr][ny] >= heights[r][j])
            {
                Dfs(nr, ny, visited);

            }
        }
    }
}