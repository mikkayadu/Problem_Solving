class Solution:
    def maximumSwap(self, num: int) -> int:
        num = [int(x) for x in str(num)]
        n = len(num)

        maxi = n - 1
        x = y= 0
        for i in range(n-1, -1, -1):
            if num[i] > num[maxi]:
                maxi = i
            elif num[i] < num[maxi]:
                x = i
                y = maxi
        
        num[x], num[y] = num[y], num[x]
        return int(''.join([str(x) for x in num]))


        
