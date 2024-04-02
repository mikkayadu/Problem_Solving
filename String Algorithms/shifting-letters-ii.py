class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0] * (len(s) + 2)
        
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        
        for a, b, k in shifts:
            if k== 1:
                arr[a + 1] = (arr[a+1] + 1)
                arr[b+2] = (arr[b+2] - 1) 
            else:
                arr[a + 1] = (arr[a+1] - 1)
                arr[b+2] = (arr[b+2] + 1 )
        
        for i in range(1, len(arr)):
            arr[i] += arr[i-1]
        print("arr", arr)
        ans = ""
        for i in range(1, len(arr)-1):
            if arr[i] >= 0:
                ans += alphabets[(alphabets.index(s[i-1]) + arr[i]) % 26]
            else:
                ans += alphabets[(alphabets.index(s[i-1]) - abs(arr[i]) %26)]
            


        return ans
