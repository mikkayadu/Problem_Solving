public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {
        int n = temperatures.Length;
        Stack<int> stack = new Stack<int> ();
        int[] ans = new int[n] ;

        for (int r = 0; r < n ; r ++)
        {
            int temp = temperatures[r];

            while (stack.Count != 0 && temperatures[stack.Peek()] < temp)
            {
                int idx = stack.Pop();
                ans[idx] = r - idx;
            }

            stack.Push(r);


        }

        return ans;
        
    }
}