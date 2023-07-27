t = int(input())
 
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
 
    arr.sort()
    for i in range(n-1):
        if abs(arr[i+1] - arr[i]) <= 1:
            arr[i] = -1
    ans = [num for num in arr if num != -1]
 
    if len(ans) == 1:
        print("YES")
    else:
        print("NO")
