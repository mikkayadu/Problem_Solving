public class Solution {
    public bool ValidMountainArray(int[] arr) {
        int maxi = 0;
        int n = arr.Length;

        for (int i= 0; i < n-1; i ++ )
        {
            if (arr[i] >= arr[i+1])
            {
                maxi = i;
                break;
            }
        }

        if (maxi == 0)
            return false;

        for (int i = maxi; i < n-1; i++)
        {
            if (arr[i] <= arr[i+1])
                return false;
        }
        
        return true;
    }
}