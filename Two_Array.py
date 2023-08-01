t = int(input())
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort(); b.sort()
    # if a == b:
    #     return "YES"
    
    for i in range(n):
        if a[i]-b[i] > 0 or a[i]-b[i]<-1:
            return "NO"
    return "YES"

for _ in range(t):
    print(solve())
