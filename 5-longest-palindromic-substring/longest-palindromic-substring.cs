public class Solution {
    public string LongestPalindrome(string s) {
        string ans = ""; 
        int maxi = 0; 
        int n = s.Length;

        for (int i =0; i < n; i++)
        {
            var (l, r) = (i, i);

            while ( l >= 0 && r < n && s[l] == s[r])
            {
                l-- ; r++;
            }

            if (r -l -1 > maxi)
            {
                ans = s[(l+1)..r];
                maxi = r -l -1;
            }

            l = i;  r = i+1;

            while ( l >= 0 && r < n && s[l] == s[r])
            {
                l--; r++;
            }

            if (r -l -1 > maxi)
            {
                ans = s[(l+1)..r];
                maxi = r -l -1;
            }
        }

        
        return ans;    
    }
}