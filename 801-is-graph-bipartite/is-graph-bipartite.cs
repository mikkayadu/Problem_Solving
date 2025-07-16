public class Solution {
    public bool IsBipartite(int[][] graph) {
        int n = graph.Length;
        int[] color = new int[n];
        Array.Fill(color, -1);

        

        bool result = true;

        for (int i =0; i<n; i++){
            if (color[i] == -1)
            {
                color[i] = 0;
                result = result && Dfs(i, graph, color);
            }
        }

        return result;
        
    }

    public bool Dfs(int node, int[][] graph, int[] color){
            bool temp = true;

            foreach(var nei in graph[node])
            {
                if (color[nei] == -1){
                    color[nei] = 1 - color[node];
                    temp = temp && Dfs(nei, graph, color);
                }

                else if (color[nei] == color[node])
                    return false;
            }

            return temp;
        }
}