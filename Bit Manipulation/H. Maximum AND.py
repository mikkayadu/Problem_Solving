t = int(input())
 
def solve():
        n, k  = list(map(int, input().split()))
        a = list(map(int, input().split()))
        ans = ""
 
        for i in range(30, -1, -1):
            count = 0
            for j in range(len(a)):
                num = a[j]
                if num & (1<<i) == 0:
                        count += 1
            if count <= k:
                k-= count
                ans += "1"
            else:
                ans += "0"
        
        
        return int(ans, 2)
             
 
 
for _ in range(t):
    print(solve())
