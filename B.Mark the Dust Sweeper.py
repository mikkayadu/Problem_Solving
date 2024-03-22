t = int(input())

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0

    
    flag = False
    for i in range(len(arr)-1):
        if arr[i]!= 0:
            ans += arr[i]
            flag = True
        
        elif flag :
            ans += 1
    return ans

for _ in range(t):
    print(solve())
