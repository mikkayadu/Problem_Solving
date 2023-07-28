n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()
 
if k == 0:
    
    ans = arr[k] -1 if arr[k] -1 !=0 else "-1"
    print(ans)
else:
    if k == n:
        print(arr[-1] )
    elif arr[k-1] == arr[k]:
        print("-1")
    else:
        print(arr[k]-1)



"""
C= 1200
"""
