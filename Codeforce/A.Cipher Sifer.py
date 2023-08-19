t  = int(input())
for _ in range(t):
    n = int(input())
    a = list(input())
    ans = ""

    l, r = 0, 0
    while r<n:
        if l != r and a[r] == a[l]:
            ans+= a[l]
            l=r+1
        r+=1
    print(ans)
