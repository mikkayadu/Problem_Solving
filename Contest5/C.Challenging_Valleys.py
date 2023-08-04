t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    arr = []
    l = 0
    
 
    for x in a:
        if not arr or arr[-1] != x:
            arr.append(x)
    
    valley = 0
    for i in range(len(arr)):
        if ((i == 0 or arr[i] < arr[i - 1]) and (i == len(arr) - 1 or arr[i] < arr[i + 1])):
            valley+=1
    
 
    
 
    
        
    
    print("YES" if valley == 1 else "NO")
