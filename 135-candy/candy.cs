
public class Solution {
    public int Candy(int[] ratings) {
        int[] lst = Enumerable.Repeat(1, ratings.Length).ToArray();

        for (int i=0; i < ratings.Length -1; i++){
            if (ratings[i+1] > ratings[i]){
                lst[i+1] = lst[i] + 1;
            }
        }


        for (int i=ratings.Length -2 ; i >= 0; i --){
            if (ratings[i] > ratings[i+1]){
                lst[i] = Math.Max(lst[i], lst[i+1] + 1);
            }
        }


        return lst.Sum();

    }
}