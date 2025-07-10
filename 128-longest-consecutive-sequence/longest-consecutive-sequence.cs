public class Solution {
    public int LongestConsecutive(int[] nums) {
        int maximum = 0;
        int count = 1; 
        int track = 1; 

        HashSet<int> nums_set = new HashSet<int>(nums);

        foreach(var num in nums_set){
            if (!nums_set.Contains(num - 1) ){
                count = 1;


                while (nums_set.Contains(num + track)){
                    track ++;
                    count ++;
                }
                track = 1;
            maximum = Math.Max(count, maximum);
            count = 0;
            }

        
        }
        return maximum;
        
    }
}